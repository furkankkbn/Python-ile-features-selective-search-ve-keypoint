# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(763, 590)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 770, 601))
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
"background: #F9F9F9;\n"
"border: 1px solid #C4C4C3;\n"
"min-width: 20ex;\n"
"padding: 7px;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"background: #F9F9F9;\n"
"}\n"
"QTabBar::tab:selected {\n"
"background: white;\n"
"border-bottom: 0px solid #C2C7CB;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"margin-top: 3px; /* make non-selected tabs look smaller */\n"
"border-left:0px;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_45 = QtWidgets.QLabel(self.tab)
        self.label_45.setGeometry(QtCore.QRect(20, 30, 151, 16))
        self.label_45.setObjectName("label_45")
        self.btn_histogram_uygula = QtWidgets.QPushButton(self.tab)
        self.btn_histogram_uygula.setGeometry(QtCore.QRect(280, 390, 91, 31))
        self.btn_histogram_uygula.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_histogram_uygula.setObjectName("btn_histogram_uygula")
        self.img_histogram_kaynak = QtWidgets.QGraphicsView(self.tab)
        self.img_histogram_kaynak.setGeometry(QtCore.QRect(20, 70, 351, 311))
        self.img_histogram_kaynak.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_histogram_kaynak.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_histogram_kaynak.setObjectName("img_histogram_kaynak")
        self.img_histogram_sonuc = QtWidgets.QGraphicsView(self.tab)
        self.img_histogram_sonuc.setGeometry(QtCore.QRect(390, 70, 351, 311))
        self.img_histogram_sonuc.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_histogram_sonuc.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_histogram_sonuc.setObjectName("img_histogram_sonuc")
        self.label_46 = QtWidgets.QLabel(self.tab)
        self.label_46.setGeometry(QtCore.QRect(390, 30, 151, 16))
        self.label_46.setObjectName("label_46")
        self.btn_histogram_yukle = QtWidgets.QPushButton(self.tab)
        self.btn_histogram_yukle.setGeometry(QtCore.QRect(340, 350, 31, 31))
        self.btn_histogram_yukle.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_histogram_yukle.setObjectName("btn_histogram_yukle")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.img_template_aranan = QtWidgets.QGraphicsView(self.tab_2)
        self.img_template_aranan.setGeometry(QtCore.QRect(20, 70, 221, 201))
        self.img_template_aranan.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_template_aranan.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_template_aranan.setObjectName("img_template_aranan")
        self.label_47 = QtWidgets.QLabel(self.tab_2)
        self.label_47.setGeometry(QtCore.QRect(20, 30, 151, 16))
        self.label_47.setObjectName("label_47")
        self.btn_template_aranan_yukle = QtWidgets.QPushButton(self.tab_2)
        self.btn_template_aranan_yukle.setGeometry(QtCore.QRect(210, 240, 31, 31))
        self.btn_template_aranan_yukle.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_template_aranan_yukle.setObjectName("btn_template_aranan_yukle")
        self.img_template_kaynak = QtWidgets.QGraphicsView(self.tab_2)
        self.img_template_kaynak.setGeometry(QtCore.QRect(280, 70, 221, 201))
        self.img_template_kaynak.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_template_kaynak.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_template_kaynak.setObjectName("img_template_kaynak")
        self.btn_template_kaynak_yukle = QtWidgets.QPushButton(self.tab_2)
        self.btn_template_kaynak_yukle.setGeometry(QtCore.QRect(470, 240, 31, 31))
        self.btn_template_kaynak_yukle.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_template_kaynak_yukle.setObjectName("btn_template_kaynak_yukle")
        self.label_48 = QtWidgets.QLabel(self.tab_2)
        self.label_48.setGeometry(QtCore.QRect(280, 30, 151, 16))
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.tab_2)
        self.label_49.setGeometry(QtCore.QRect(520, 30, 151, 16))
        self.label_49.setObjectName("label_49")
        self.img_template_sonuc = QtWidgets.QGraphicsView(self.tab_2)
        self.img_template_sonuc.setGeometry(QtCore.QRect(520, 70, 221, 201))
        self.img_template_sonuc.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_template_sonuc.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_template_sonuc.setObjectName("img_template_sonuc")
        self.btn_template_uygula = QtWidgets.QPushButton(self.tab_2)
        self.btn_template_uygula.setGeometry(QtCore.QRect(520, 290, 221, 51))
        self.btn_template_uygula.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_template_uygula.setObjectName("btn_template_uygula")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 340, 221, 101))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_22 = QtWidgets.QLabel(self.groupBox_6)
        self.label_22.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.label_22.setObjectName("label_22")
        self.lbl_template_SSIM = QtWidgets.QLabel(self.groupBox_6)
        self.lbl_template_SSIM.setGeometry(QtCore.QRect(80, 47, 111, 21))
        self.lbl_template_SSIM.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;")
        self.lbl_template_SSIM.setObjectName("lbl_template_SSIM")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.table_keypoint_referans = QtWidgets.QTableWidget(self.tab_4)
        self.table_keypoint_referans.setGeometry(QtCore.QRect(20, 60, 521, 191))
        self.table_keypoint_referans.setObjectName("table_keypoint_referans")
        self.table_keypoint_referans.setColumnCount(0)
        self.table_keypoint_referans.setRowCount(0)
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 221, 16))
        self.label_4.setObjectName("label_4")
        self.btn_keypoint_referance_points = QtWidgets.QPushButton(self.tab_4)
        self.btn_keypoint_referance_points.setGeometry(QtCore.QRect(510, 220, 31, 31))
        self.btn_keypoint_referance_points.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_keypoint_referance_points.setObjectName("btn_keypoint_referance_points")
        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox.setGeometry(QtCore.QRect(560, 40, 181, 211))
        self.groupBox.setObjectName("groupBox")
        self.cmb_keypoint_algorithm = QtWidgets.QComboBox(self.groupBox)
        self.cmb_keypoint_algorithm.setGeometry(QtCore.QRect(20, 70, 141, 31))
        self.cmb_keypoint_algorithm.setStyleSheet("border:1px solid black;")
        self.cmb_keypoint_algorithm.setObjectName("cmb_keypoint_algorithm")
        self.cmb_keypoint_algorithm.addItem("")
        self.cmb_keypoint_algorithm.addItem("")
        self.cmb_keypoint_algorithm.addItem("")
        self.btn_keypoint_apply = QtWidgets.QPushButton(self.groupBox)
        self.btn_keypoint_apply.setGeometry(QtCore.QRect(20, 120, 141, 61))
        self.btn_keypoint_apply.setStyleSheet("border: 1px solid red;\n"
"color:red;\n"
"")
        self.btn_keypoint_apply.setObjectName("btn_keypoint_apply")
        self.label_53 = QtWidgets.QLabel(self.groupBox)
        self.label_53.setGeometry(QtCore.QRect(20, 40, 151, 16))
        self.label_53.setObjectName("label_53")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setGeometry(QtCore.QRect(300, 300, 241, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.img_keypoint_result = QtWidgets.QGraphicsView(self.groupBox_2)
        self.img_keypoint_result.setGeometry(QtCore.QRect(5, 17, 231, 208))
        self.img_keypoint_result.setStyleSheet("border:0px;")
        self.img_keypoint_result.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_keypoint_result.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_keypoint_result.setObjectName("img_keypoint_result")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_3.setGeometry(QtCore.QRect(560, 300, 181, 131))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(20, 62, 71, 16))
        self.label_5.setObjectName("label_5")
        self.lbl_keypoint_img_count = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_keypoint_img_count.setGeometry(QtCore.QRect(100, 60, 61, 21))
        self.lbl_keypoint_img_count.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;")
        self.lbl_keypoint_img_count.setObjectName("lbl_keypoint_img_count")
        self.lbl_keypoint_point_count = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_keypoint_point_count.setGeometry(QtCore.QRect(100, 90, 61, 21))
        self.lbl_keypoint_point_count.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;")
        self.lbl_keypoint_point_count.setObjectName("lbl_keypoint_point_count")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(20, 92, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(100, 31, 31, 16))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 5pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(130, 31, 31, 16))
        self.label_2.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: rgb(0,0,0);\n"
"font: 5pt \"MS Shell Dlg 2\";\n"
"border: 1px solid black;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_4.setGeometry(QtCore.QRect(560, 440, 181, 91))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(20, 30, 47, 13))
        self.label_6.setObjectName("label_6")
        self.lbl_keypoint_jaccard = QtWidgets.QLabel(self.groupBox_4)
        self.lbl_keypoint_jaccard.setGeometry(QtCore.QRect(20, 55, 141, 21))
        self.lbl_keypoint_jaccard.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;\n"
"padding-right:5px;")
        self.lbl_keypoint_jaccard.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_keypoint_jaccard.setObjectName("lbl_keypoint_jaccard")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 300, 261, 231))
        self.groupBox_5.setObjectName("groupBox_5")
        self.table_keypoint_result = QtWidgets.QTableWidget(self.groupBox_5)
        self.table_keypoint_result.setGeometry(QtCore.QRect(5, 25, 251, 201))
        self.table_keypoint_result.setStyleSheet("border:0px;")
        self.table_keypoint_result.setObjectName("table_keypoint_result")
        self.table_keypoint_result.setColumnCount(0)
        self.table_keypoint_result.setRowCount(0)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_3 = QtWidgets.QLabel(self.tab_5)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label_3.setObjectName("label_3")
        self.table_features = QtWidgets.QTableWidget(self.tab_5)
        self.table_features.setGeometry(QtCore.QRect(20, 50, 391, 411))
        self.table_features.setObjectName("table_features")
        self.table_features.setColumnCount(0)
        self.table_features.setRowCount(0)
        self.btn_features_apply = QtWidgets.QPushButton(self.tab_5)
        self.btn_features_apply.setGeometry(QtCore.QRect(640, 490, 101, 31))
        self.btn_features_apply.setStyleSheet("border: 1px solid red;\n"
"color:red;\n"
"")
        self.btn_features_apply.setObjectName("btn_features_apply")
        self.lbl_features_count = QtWidgets.QLabel(self.tab_5)
        self.lbl_features_count.setGeometry(QtCore.QRect(150, 500, 61, 16))
        self.lbl_features_count.setObjectName("lbl_features_count")
        self.label_51 = QtWidgets.QLabel(self.tab_5)
        self.label_51.setGeometry(QtCore.QRect(20, 500, 121, 16))
        self.label_51.setObjectName("label_51")
        self.label_9 = QtWidgets.QLabel(self.tab_5)
        self.label_9.setGeometry(QtCore.QRect(430, 20, 71, 16))
        self.label_9.setObjectName("label_9")
        self.table_features_y = QtWidgets.QTableWidget(self.tab_5)
        self.table_features_y.setGeometry(QtCore.QRect(430, 50, 101, 411))
        self.table_features_y.setObjectName("table_features_y")
        self.table_features_y.setColumnCount(0)
        self.table_features_y.setRowCount(0)
        self.label_10 = QtWidgets.QLabel(self.tab_5)
        self.label_10.setGeometry(QtCore.QRect(550, 20, 71, 16))
        self.label_10.setObjectName("label_10")
        self.table_features_labels = QtWidgets.QTableWidget(self.tab_5)
        self.table_features_labels.setGeometry(QtCore.QRect(550, 50, 191, 411))
        self.table_features_labels.setObjectName("table_features_labels")
        self.table_features_labels.setColumnCount(0)
        self.table_features_labels.setRowCount(0)
        self.cmb_features_algorithm = QtWidgets.QComboBox(self.tab_5)
        self.cmb_features_algorithm.setGeometry(QtCore.QRect(550, 490, 71, 31))
        self.cmb_features_algorithm.setStyleSheet("border:1px solid black;")
        self.cmb_features_algorithm.setObjectName("cmb_features_algorithm")
        self.cmb_features_algorithm.addItem("")
        self.cmb_features_algorithm.addItem("")
        self.cmb_features_algorithm.addItem("")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_45.setText(_translate("MainWindow", "K a y n a k  R e s i m"))
        self.btn_histogram_uygula.setText(_translate("MainWindow", "E Ş İ T L E"))
        self.label_46.setText(_translate("MainWindow", "S o n u ç  R e s i m"))
        self.btn_histogram_yukle.setText(_translate("MainWindow", "↓"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Histogram Eşitleme"))
        self.label_47.setText(_translate("MainWindow", "A r a n a c a k  R e s i m"))
        self.btn_template_aranan_yukle.setText(_translate("MainWindow", "↓"))
        self.btn_template_kaynak_yukle.setText(_translate("MainWindow", "↓"))
        self.label_48.setText(_translate("MainWindow", "K a y n a k  R e s i m"))
        self.label_49.setText(_translate("MainWindow", "B u l u n a n  R e s i m"))
        self.btn_template_uygula.setText(_translate("MainWindow", "U Y G U L A"))
        self.groupBox_6.setTitle(_translate("MainWindow", "K a r ş ı l a ş t ı r m a  D e ğ e r"))
        self.label_22.setText(_translate("MainWindow", "SSIM :"))
        self.lbl_template_SSIM.setText(_translate("MainWindow", "-"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Template Matching"))
        self.label_4.setText(_translate("MainWindow", "R e f e r a n s  (Grand Truthk) Kordinatlar:"))
        self.btn_keypoint_referance_points.setText(_translate("MainWindow", "↓"))
        self.groupBox.setTitle(_translate("MainWindow", "İ ş l e m l e r"))
        self.cmb_keypoint_algorithm.setItemText(0, _translate("MainWindow", "SURF"))
        self.cmb_keypoint_algorithm.setItemText(1, _translate("MainWindow", "SIFT"))
        self.cmb_keypoint_algorithm.setItemText(2, _translate("MainWindow", "ORB"))
        self.btn_keypoint_apply.setText(_translate("MainWindow", "U Y G U L A"))
        self.label_53.setText(_translate("MainWindow", "Algoritmalar :"))
        self.groupBox_2.setTitle(_translate("MainWindow", "R e t i n a  O p t i k  D i s k"))
        self.groupBox_3.setTitle(_translate("MainWindow", "B i l g i l e n d i r m e"))
        self.label_5.setText(_translate("MainWindow", "Resim Sayısı :"))
        self.lbl_keypoint_img_count.setText(_translate("MainWindow", "-"))
        self.lbl_keypoint_point_count.setText(_translate("MainWindow", "-"))
        self.label_7.setText(_translate("MainWindow", "Point Sayısı :"))
        self.label_8.setText(_translate("MainWindow", "Renklendirme :"))
        self.label.setText(_translate("MainWindow", "referans"))
        self.label_2.setText(_translate("MainWindow", "sonuç"))
        self.groupBox_4.setTitle(_translate("MainWindow", "K a r ş ı l a ş t ı r m a "))
        self.label_6.setText(_translate("MainWindow", "Jaccard :"))
        self.lbl_keypoint_jaccard.setText(_translate("MainWindow", "-"))
        self.groupBox_5.setTitle(_translate("MainWindow", "S o n u ç l a r"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Key Point"))
        self.label_3.setText(_translate("MainWindow", "F e a t u r e s"))
        self.btn_features_apply.setText(_translate("MainWindow", "U Y G U L A"))
        self.lbl_features_count.setText(_translate("MainWindow", "0"))
        self.label_51.setText(_translate("MainWindow", "Tamlanan resim sayısı :"))
        self.label_9.setText(_translate("MainWindow", "y  L i s t"))
        self.label_10.setText(_translate("MainWindow", "L a b e l s"))
        self.cmb_features_algorithm.setItemText(0, _translate("MainWindow", "Gabor"))
        self.cmb_features_algorithm.setItemText(1, _translate("MainWindow", "GLCM"))
        self.cmb_features_algorithm.setItemText(2, _translate("MainWindow", "Daisy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Features"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Kaçak Yapı [BONUS]"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

