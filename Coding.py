from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5 import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget,QTableWidget,QTableWidgetItem,QGraphicsScene,QGraphicsPixmapItem,QFileDialog
from Design import Ui_MainWindow

import os
import io as _io
import cv2
import math
import numpy as np
import matplotlib.pyplot as plt
from xlrd import open_workbook
from openpyxl.reader.excel import load_workbook

from skimage import data, img_as_float,io
from skimage.measure import compare_ssim as SSIM2

from sklearn.metrics import mean_squared_error as MSE
from PIL import Image
import scipy
import pandas as pd
from scipy import ndimage
from sklearn import decomposition
from skimage import data
from skimage import color
from skimage.segmentation import clear_border
from skimage.morphology import label, closing, square
from skimage.measure import regionprops
import random
import matplotlib.image as IMG
from skimage import data
from skimage.util import img_as_float
from skimage.filters import gabor_kernel
from skimage.feature import greycomatrix, greycoprops
from skimage import data
from PIL.ImageQt import ImageQt
from skimage.feature import daisy
import pickle
from sklearn.metrics import jaccard_similarity_score
from skimage.feature import daisy
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class override_graphicsScene (Qt.QGraphicsScene):
    def __init__(self,parent = None):
        super(override_graphicsScene,self).__init__(parent)

    def mousePressEvent(self, event):
        super(override_graphicsScene, self).mousePressEvent(event)
        print(event.pos())

class MainWindow(QWidget,Ui_MainWindow):
    
    temp_path = "image.png"
    temp_path_2 = "image_2.png"
    temp_path_3 = "image_3.png"
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.btn_histogram_yukle.clicked.connect(self.button_histogram_yukle)
        self.btn_histogram_uygula.clicked.connect(self.button_histogram_uygula)
        
        self.btn_template_aranan_yukle.clicked.connect(self.button_template_aranan_yukle)
        self.btn_template_kaynak_yukle.clicked.connect(self.button_template_kaynak_yukle)
        self.btn_template_uygula.clicked.connect(self.button_template_uygula)
        
        self.btn_features_apply.clicked.connect(self.button_features_apply)
        
        self.btn_keypoint_referance_points.clicked.connect(self.button_keypoint_referance_points)
        self.btn_keypoint_apply.clicked.connect(self.button_keypoint_apply)
        self.table_keypoint_result.cellClicked.connect(self.onSelected)
    
    
        
    def onSelected(self,row,column):
        image_name = self.table_keypoint_result.item(row,0).text()
        scene = self.show_image_path(self.directory_retina_result+"/"+image_name,self.img_keypoint_result.size())
        self.img_keypoint_result.setScene(scene)
        
        jaccard_score = self.table_keypoint_result.item(row,5).text()
        self.lbl_keypoint_jaccard.setText(jaccard_score)
        
    
    #HİSTOGRAM UYGULAMA ----------------------------------------------------------------------
         
    def button_histogram_yukle(self):


    def hist_topla(self,h):
    	return [sum(h[:i+1]) for i in range(len(h))]
    
    def hist_img(self,im):
    	m, n = im.shape
    	h = [0.0] * 256
    	for i in range(m):
    		for j in range(n):
    			h[im[i, j]]+=1
    	return np.array(h)/(m*n)
    
    def hist_sonuc(self,im):
    	h = self.hist_img(im)
    	cdf = np.array(self.hist_topla(h))
    	sk = np.uint8(255 * cdf)
    	s1, s2 = im.shape
    	Y = np.zeros_like(im)
    
    	for i in range(0, s1):
    		for j in range(0, s2):
    			Y[i, j] = sk[im[i, j]]
    	H = self.hist_img(Y)
    	return Y , h, H, sk

        
    def button_histogram_uygula(self):  
        img = np.uint8(IMG.imread(self.temp_path)*255.0)
        
        img = np.uint8((0.2126* img[:,:,0]) + \
          		np.uint8(0.7152 * img[:,:,1]) +\
        			 np.uint8(0.0722 * img[:,:,2]))
        
        new_img, h, new_h, sk = self.hist_sonuc(img)
        img = color.rgb2gray(new_img)
        cv2.imwrite(self.temp_path_2,img)
        
        scene = self.show_image_path(self.temp_path_2,self.img_histogram_sonuc.size())
        self.img_histogram_sonuc.setScene(scene)


    #TEMPLATE MATCHING --------------------------------------------------------
    def button_template_aranan_yukle(self):
        file,_ = QFileDialog.getOpenFileName(self, 'Open file', './',"Image files (*.png *.gif)")
        file_image = Image.open(file)
        file_image.save(self.temp_path)
        scene = QGraphicsScene()
        scene = self.show_image_path(self.temp_path,self.img_template_aranan.size())
        self.img_template_aranan.setScene(scene)

    def button_template_kaynak_yukle(self):
        file,_ = QFileDialog.getOpenFileName(self, 'Open file', './',"Image files (*.png *.gif)")
        file_image = Image.open(file)
        file_image.save(self.temp_path_2)
        scene = QGraphicsScene()
        scene = self.show_image_path(self.temp_path_2,self.img_template_kaynak.size())
        self.img_template_kaynak.setScene(scene)

    def button_template_uygula(self):
        list_score = []
        temp_score_ssim = 0
        temp_score_mse = 0
        temp_best_score_ssim = 0
        temp_best_score_mse = 0
        temp_crop = 0
        
        aranan = Image.open(self.temp_path)
        #aranan = color.rgb2gray(aranan)
        aranan_w,aranan_h = aranan.size
        IMG.imsave(self.temp_path,aranan)
        
        kaynak = cv2.imread(self.temp_path_2)
        #kaynak = color.rgb2gray(kaynak)
        kaynak_w,kaynak_h,c = kaynak.shape
        #IMG.imsave(self.temp_path,aranan)
        print("kaynak genişlik: ",kaynak_w)

        
        for j,h in enumerate(range(0,kaynak_h)):
            for i,w in enumerate(range(0,kaynak_w)):
                #print(w,h)
                #yukarıdan aşağıya
                #w1,w2 = 0+w,aranan_w
                #h1,h2 = aranan_h+w,0+h
                if((kaynak_w - w) > aranan_w):
                    w1,w2 = 0+h,aranan_w+w
                    h1,h2 = aranan_h+h,0+w
                    
                    crop = kaynak[w1:h1, h2:w2]
                    
                    #IMG.imsave(self.temp_path_3,crop)
                    #IMG.imsave("./imgs/_"+str(w)+".png",crop)
                    
                    #crop_w,crop_h=h2-w2,w1-h1
                    #if(aranan_w==crop_w*-1 and aranan_h==crop_h*-1):
                    temp_score_ssim = self.ssim(aranan,crop)
                    #temp_score_mse = self.mse(self.temp_path,self.temp_path_3)

                    try:
                        if(temp_score_ssim>temp_best_score_ssim):
                            temp_best_score_ssim = temp_score_ssim
                            temp_best_score_mse = temp_score_mse
                            temp_crop = crop
                    except ValueError:
                        print("Invalid Entry - try again")

        IMG.imsave(self.temp_path_3,temp_crop)
        scene = self.show_image_path(self.temp_path_3,self.img_template_sonuc.size())
        self.img_template_sonuc.setScene(scene)  
        self.lbl_template_SSIM.setText(str(temp_best_score_ssim))
        #self.lbl_template_SSIM.setText(str(temp_best_score_mse))
                
        
    #FEATURES
    directory = "./objects/features/"
    path = "./objects/features/"

    def button_features_apply(self):
        self.table_features.clear()
        self.table_features_labels.clear()
        self.table_features_y.clear()
        
        features = []
        features += [0 for i in range(0,100)]
        
        features_label = []
        
        list_x,list_y=[],[]
        x,y=[],[]
        j = 0
        
        count_features = 0
        
        folder_list = os.listdir(self.directory)
        for i,folder in enumerate(folder_list):
            files_list = os.listdir(self.path+folder)
            #print("folder",folder)
            #print("files",files_list)
            
            features_label.append([folder,i])
            
            for j,file in enumerate(files_list):

                img = cv2.imread(self.directory+folder+"/"+file, cv2.COLOR_BGR2GRAY)
                #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                #print(str(self.directory+folder+"/"+file))
                
                if(self.cmb_features_algorithm.currentIndex() == 0):
                    desc = self.gabor_features(img,self.build_filters())
                    d = decomposition.PCA(2).fit_transform(desc)
                    #print(str(j),"----------------\n",d)
                    list_x.append([d[0][0],d[0][1]])
                    d_temp = np.array([d[0][0],d[0][1]])
                if(self.cmb_features_algorithm.currentIndex() == 1):
                    desc = greycomatrix(img, [2], [0], 256, symmetric=True, normed=True)
                    desc = desc.flatten()
                    list_x.append([desc[0],desc[len(desc)-1]])
                    d_temp = np.array(desc)
                if(self.cmb_features_algorithm.currentIndex() == 2):
                    desc, descs_img = daisy(img, step=2, radius=2, rings=1, histograms=3, orientations=3, visualize=True)               
                    #print(desc)
                    #d = decomposition.PCA(2).fit_transform(desc)
                    d = decomposition.PCA(2).fit_transform(desc)
                    print(d)
                    break
                    list_x.append(desc)
                    d_temp = np.array(desc)
                    
                list_y.append(file)
                y.append(int(i))
                features[j]=d_temp
                j+=1
                               
                count_features += 1
                self.lbl_features_count.setText(str(count_features))
        
        features = np.array(features)
        #print(list_x)
        #print("--------------------")
        #print(features)
        
        print("x boyut:",str(len(list_x)))
        
        self.table_features.setColumnCount(len(list_x[0])) #len(features[0])
        self.table_features.setRowCount(len(list_x))

        for _i,row in enumerate(list_x):
            for _j,value in enumerate(row):
                self.table_features.setItem(_i,_j, QTableWidgetItem(str(value)))
                #break
        self.table_features.horizontalHeader().setStretchLastSection(True)
        self.table_features.resizeColumnsToContents()
        self.table_features.setHorizontalHeaderLabels(['feature_1','feature_2'])
        
        #print(y)
        self.table_features_y.setColumnCount(1)
        self.table_features_y.setRowCount(len(y))
        for _i,row in enumerate(y):
            self.table_features_y.setItem(_i,0, QTableWidgetItem(str(row)))
        self.table_features_y.horizontalHeader().setStretchLastSection(True)
        self.table_features_y.resizeColumnsToContents()
        self.table_features_y.setHorizontalHeaderLabels(['y'])
        
        #print(features_label)
        self.table_features_labels.setColumnCount(len(features_label[0]))
        self.table_features_labels.setRowCount(len(features_label))
        for _i,row in enumerate(features_label):
            for _j, value in enumerate(row):
                self.table_features_labels.setItem(_i,_j, QTableWidgetItem(str(value)))
        self.table_features_labels.horizontalHeader().setStretchLastSection(True)
        self.table_features_labels.resizeColumnsToContents()
        self.table_features_labels.setHorizontalHeaderLabels(['Label','Key'])
        
        X_train, X_test, y_train, y_test = train_test_split(list_x, y, test_size = 1/3, random_state = 0)
            
        accurity = self.ALGORITHM_RANDOM_FOREST(X_train, X_test, y_train, y_test)
        print("Başarı oranı:",str(accurity))


    def ALGORITHM_RANDOM_FOREST(self,_x_train,_x_test,_y_train,_y_test):
        model = RandomForestClassifier()
        model.fit(_x_train,_y_train)
        y_pred = model.predict(_x_test)
        accurity = accuracy_score(_y_test,y_pred)
        return str(round(accurity*100,2))

    def build_filters(self):
        filters = []
        ksize = 31
        for theta in np.arange(0, np.pi, np.pi / 16):
            kern = cv2.getGaborKernel((ksize, ksize), 4.0, theta, 10.0, 0.5, 0, ktype=cv2.CV_32F)
        kern /= 1.5*kern.sum()
        filters.append(kern)
        return filters
         
    def gabor_features(self,img, filters):
        accum = np.zeros_like(img)
        for kern in filters:
            fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
        np.maximum(accum, fimg, accum)
        return accum

    #KEY POİNT OPTİK DİSK RETİNA
    referance_file = ""
    referance_data = []
    def button_keypoint_referance_points(self):
        file,_ = QFileDialog.getOpenFileName(self, 'Open file', './',"Pkl Files (*.pkl *.)")
        self.referance_file = file
        self.referance_data=[]
        
        with open(self.referance_file, 'rb') as f:
            data = pickle.load(f)
        
        self.table_keypoint_referans.setColumnCount(len(data["image001.png"])+1)
        self.table_keypoint_referans.setRowCount(len(data))
        for i,row in enumerate(data):
            referance_temp=[]
            referance_temp.append(row)
            self.table_keypoint_referans.setItem(i,0, QTableWidgetItem(str(row)))
            for j, value in enumerate(data[row]):
                self.table_keypoint_referans.setItem(i,j+1, QTableWidgetItem(str(value)))
                referance_temp.append(value)
            
            self.referance_data.append(referance_temp)
        
        self.table_keypoint_referans.horizontalHeader().setStretchLastSection(True)
        self.table_keypoint_referans.resizeColumnsToContents()
        self.table_keypoint_referans.setHorizontalHeaderLabels(self.label_header_keypoint)
        self.lbl_keypoint_img_count.setText(str(len(data)))
        
        #print(self.referance_data)
        
    
    directory_retina_source = "./objects/retina/sources/"
    directory_retina_result = "./objects/retina/results/"
    directory_retina_threshold = "./objects/retina/threshold/"
    directory_retina_clahe = "./objects/retina/clahe/"
    directory_retina_sobel = "./objects/retina/sobel/"

    label_header_keypoint = ['Image','y','x','size','Best Score','Jaccard']
    def button_keypoint_apply(self):
        
        self.table_keypoint_result.clear()
        
        results=[]
        count_point=0
        
        dec = cv2.xfeatures2d.SURF_create()
        
        if(self.cmb_keypoint_algorithm.currentIndex() == 0):
            dec = cv2.xfeatures2d.SURF_create()
        if(self.cmb_keypoint_algorithm.currentIndex() == 1):
            dec = cv2.xfeatures2d.SIFT_create()
        if(self.cmb_keypoint_algorithm.currentIndex() == 2):
            dec = cv2.ORB_create(nfeatures=1500)
        
        #files = os.listdir(self.directory_retina)
        for i,value in enumerate(self.referance_data):
            temp_img_source = cv2.imread(self.directory_retina_source+value[0])
            img_referance = cv2.imread(self.directory_retina_source+value[0],cv2.COLOR_BGR2GRAY)
            img_referance = self.get_crop(img_referance,value[2],value[1],value[3])
            img_source = cv2.imread(self.directory_retina_source+value[0],cv2.COLOR_BGR2GRAY)

            img_referance = self.step_I(img_referance,None)
            img_source = self.step_I(img_source,self.directory_retina_clahe+value[0])




            keypoints, descriptors = dec.detectAndCompute(img_source, None)
            best_score = 0
            jaccard_score = 0
            ref_x,ref_y,ref_r = self.referance_data[i][2],self.referance_data[i][1],self.referance_data[i][3]
            temp_name,temp_x,temp_y,temp_r='',0,0,0
            temp_img = 0
            #self.show_img(img_source)
            #self.key_show(img_source,keypoints)
            
            for index in range(len(keypoints)):
                count_point += 1
                x = int(keypoints[index].pt[0])
                y = int(keypoints[index].pt[1])
                r = value[3]
                            
                img_source_point = self.get_crop(img_source,x,y,r)
                #print("referance",value[2],value[1],value[3],"---","source",x,y,r)
                #print("referance:",img_referance.shape,"---- source:",img_source_point.shape,"(shape)")
                
                if(img_referance.shape == img_source_point.shape):
                    #self.show_img(img_source_point)
                    score = self.ssim2(img_referance,img_source_point)#jaccard_similarity_score
                    #self.show_img(img_referance)
                    #self.show_img(img_source_point)
                    if(score>best_score):
                        best_score=score
                        jaccard_score= self.jaccard(img_referance,img_source_point)
                        temp_img = img_source#img_source_point
                        temp_name = value[0]
                        #print("best-->",temp_name)
                        temp_x,temp_y,temp_r=x,y,r
            
            results.append([temp_name,temp_y,temp_x,temp_r,best_score,jaccard_score])
            #temp_img = self.get_draw_referance(temp_img,temp_x,temp_y,temp_r)
            temp_img = self.get_draw_referance(temp_img_source,ref_x,ref_y,ref_r)
            temp_img = self.get_draw_result(temp_img,temp_x,temp_y,temp_r)
            #print("file-->",self.directory_retina_result+temp_name)
            #IMG.imsave(self.directory_retina_result+temp_name,temp_img)
            cv2.imwrite(self.directory_retina_result+temp_name,temp_img)
    
        self.table_keypoint_result.setColumnCount(len(results[0]))
        self.table_keypoint_result.setRowCount(len(results))
        for i,row in enumerate(results):
            for j, value in enumerate(row):
                self.table_keypoint_result.setItem(i,j, QTableWidgetItem(str(value)))
        
        self.table_keypoint_result.horizontalHeader().setStretchLastSection(True)
        self.table_keypoint_result.resizeColumnsToContents()
        self.table_keypoint_result.setHorizontalHeaderLabels(self.label_header_keypoint)
        
        self.lbl_keypoint_point_count.setText(str(count_point))
        
    
    def step_II(self,img,path):
        teval,img = cv2.threshold(img,10,255, cv2.THRESH_BINARY)
        if(path != None):
            cv2.imwrite(path,img)
        return img
    
    def step_I(self,img,path):
        #img = color.rgb2gray(img)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
        img = cv2.split(img)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        img = clahe.apply(img[0])
        if(path != None):
            cv2.imwrite(path,img)
        return img
    
    def step_III(self,img,path):
        img = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
        if(path != None):
            cv2.imwrite(path,img)
        return img
    
    def get_crop(self,img,x,y,r):
        w1,h1=x-r,y-r
        w2,h2 = x+r,y+r
        img = img[h1:h2, w1:w2]
        return img
    
    def get_draw_referance(self,img,x,y,r):
        cv2.circle(img,(x, y), r, (0,0,0), 5)
        return img

    def get_draw_result(self,img,x,y,r):
        #3 ayıt edebilmek için
        cv2.circle(img,(x, y), r, (0,255,0), 5)
        return img
    
    def key_show(self,img,key):
        img = cv2.drawKeypoints(img, key, None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    #metodlar
    def show_image_path(self,img_path,size):
        self.pixmap = Qt.QPixmap()
        self.pixmap.load(img_path)
        self.pixmap = self.pixmap.scaled(size, Qt.Qt.KeepAspectRatioByExpanding,transformMode=QtCore.Qt.SmoothTransformation)
        self.graphicsPixmapItem = Qt.QGraphicsPixmapItem(self.pixmap)
        self.graphicsScene = override_graphicsScene(self)
        self.graphicsScene.addItem(self.graphicsPixmapItem)
        return self.graphicsScene
    
    def ssim(self,img1,img2):
        img_1 = np.asarray(img1)#cv2.imread(img1)
        img_2 = np.asarray(img2)#cv2.imread(img2)

        img_1 = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
        img_2 = cv2.cvtColor(img_2,cv2.COLOR_BGR2GRAY)
        try:
            if(not img_1 is None and not img_2 is None):
                if(img_1.size == img_2.size):
                    return round(SSIM2(img_1,img_2),2)
            else:
                return 0.0
        except ValueError:
            print("Invalid Entry - try again")
            return 0.0
        return 0.0
    
    def mse(self,img1,img2):
        img_1 = cv2.imread(img1)
        img_2 = cv2.imread(img2)
        
        e = np.sum((img_1.astype("float") - img_2.astype("float"))**2)
        e /= float(img_1.shape[0] * img_2.shape[1])
        r = round(e,2)
        return r
    
    def jaccard(self,img1,img2):
        img_true=np.array(img1).ravel()
        img_pred=np.array(img2).ravel()
        iou = jaccard_similarity_score(img_true, img_pred)
        return iou
    
    def ssim2(self,img1,img2):
        img_1 = np.asarray(img1)#cv2.imread(img1)
        img_2 = np.asarray(img2)#cv2.imread(img2)

        """img_1 = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
        img_2 = cv2.cvtColor(img_2,cv2.COLOR_BGR2GRAY)"""
        try:
            if(not img_1 is None and not img_2 is None):
                if(img_1.size == img_2.size):
                    return round(SSIM2(img_1,img_2),2)
            else:
                return 0.0
        except ValueError:
            print("Invalid Entry - try again")
            return 0.0
        return 0.0
    
    
    def mse2(self,img1,img2):
        img_1 = img1
        img_2 = img2
        
        e = np.sum((img_1.astype("float") - img_2.astype("float"))**2)
        e /= float(img_1.shape[0] * img_2.shape[1])
        r = round(e,2)
        return r
    
    def file_save(self,list_):
        with open('dataset.txt', 'w') as f:
            for item in list_:
                f.write("%s\n" % item)
    
    def show_img(self,img):
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()