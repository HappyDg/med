# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cebsGparform.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cebsGparForm(object):
    def setupUi(self, cebsGparForm):
        cebsGparForm.setObjectName("cebsGparForm")
        cebsGparForm.resize(1313, 946)
        self.groupBox_gpar_normal = QtWidgets.QGroupBox(cebsGparForm)
        self.groupBox_gpar_normal.setGeometry(QtCore.QRect(20, 90, 471, 91))
        self.groupBox_gpar_normal.setObjectName("groupBox_gpar_normal")
        self.checkBox_gpar_autoIdf = QtWidgets.QCheckBox(self.groupBox_gpar_normal)
        self.checkBox_gpar_autoIdf.setGeometry(QtCore.QRect(10, 30, 111, 16))
        self.checkBox_gpar_autoIdf.setChecked(True)
        self.checkBox_gpar_autoIdf.setObjectName("checkBox_gpar_autoIdf")
        self.lineEdit_gpar_picTti = QtWidgets.QLineEdit(self.groupBox_gpar_normal)
        self.lineEdit_gpar_picTti.setGeometry(QtCore.QRect(90, 60, 51, 20))
        self.lineEdit_gpar_picTti.setObjectName("lineEdit_gpar_picTti")
        self.label_gpar_picTti_title = QtWidgets.QLabel(self.groupBox_gpar_normal)
        self.label_gpar_picTti_title.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.label_gpar_picTti_title.setObjectName("label_gpar_picTti_title")
        self.label_gpar_picTti_min = QtWidgets.QLabel(self.groupBox_gpar_normal)
        self.label_gpar_picTti_min.setGeometry(QtCore.QRect(150, 60, 31, 16))
        self.label_gpar_picTti_min.setObjectName("label_gpar_picTti_min")
        self.checkBox_gpar_autoPic = QtWidgets.QCheckBox(self.groupBox_gpar_normal)
        self.checkBox_gpar_autoPic.setGeometry(QtCore.QRect(130, 30, 111, 16))
        self.checkBox_gpar_autoPic.setChecked(True)
        self.checkBox_gpar_autoPic.setObjectName("checkBox_gpar_autoPic")
        self.checkBox_gpar_picFixPos = QtWidgets.QCheckBox(self.groupBox_gpar_normal)
        self.checkBox_gpar_picFixPos.setGeometry(QtCore.QRect(240, 30, 71, 16))
        self.checkBox_gpar_picFixPos.setChecked(False)
        self.checkBox_gpar_picFixPos.setObjectName("checkBox_gpar_picFixPos")
        self.groupBox_gpar_pic = QtWidgets.QGroupBox(cebsGparForm)
        self.groupBox_gpar_pic.setGeometry(QtCore.QRect(200, 200, 291, 191))
        self.groupBox_gpar_pic.setObjectName("groupBox_gpar_pic")
        self.lineEdit_gpar_vision_small_low_limit = QtWidgets.QLineEdit(self.groupBox_gpar_pic)
        self.lineEdit_gpar_vision_small_low_limit.setGeometry(QtCore.QRect(100, 30, 41, 20))
        self.lineEdit_gpar_vision_small_low_limit.setObjectName("lineEdit_gpar_vision_small_low_limit")
        self.label_gpar_vision_t1 = QtWidgets.QLabel(self.groupBox_gpar_pic)
        self.label_gpar_vision_t1.setGeometry(QtCore.QRect(10, 30, 111, 21))
        self.label_gpar_vision_t1.setObjectName("label_gpar_vision_t1")
        self.lineEdit_gpar_vision_small_mid_limit = QtWidgets.QLineEdit(self.groupBox_gpar_pic)
        self.lineEdit_gpar_vision_small_mid_limit.setGeometry(QtCore.QRect(100, 60, 41, 20))
        self.lineEdit_gpar_vision_small_mid_limit.setObjectName("lineEdit_gpar_vision_small_mid_limit")
        self.label_gpar_vision_t2 = QtWidgets.QLabel(self.groupBox_gpar_pic)
        self.label_gpar_vision_t2.setGeometry(QtCore.QRect(10, 60, 111, 21))
        self.label_gpar_vision_t2.setObjectName("label_gpar_vision_t2")
        self.lineEdit_gpar_vision_mid_big_limit = QtWidgets.QLineEdit(self.groupBox_gpar_pic)
        self.lineEdit_gpar_vision_mid_big_limit.setGeometry(QtCore.QRect(100, 90, 41, 20))
        self.lineEdit_gpar_vision_mid_big_limit.setObjectName("lineEdit_gpar_vision_mid_big_limit")
        self.label_gpar_vision_t3 = QtWidgets.QLabel(self.groupBox_gpar_pic)
        self.label_gpar_vision_t3.setGeometry(QtCore.QRect(10, 90, 111, 21))
        self.label_gpar_vision_t3.setObjectName("label_gpar_vision_t3")
        self.lineEdit_gpar_vision_big_upper_limit = QtWidgets.QLineEdit(self.groupBox_gpar_pic)
        self.lineEdit_gpar_vision_big_upper_limit.setGeometry(QtCore.QRect(100, 120, 41, 20))
        self.lineEdit_gpar_vision_big_upper_limit.setObjectName("lineEdit_gpar_vision_big_upper_limit")
        self.label_gpar_vision_t4 = QtWidgets.QLabel(self.groupBox_gpar_pic)
        self.label_gpar_vision_t4.setGeometry(QtCore.QRect(10, 120, 111, 21))
        self.label_gpar_vision_t4.setObjectName("label_gpar_vision_t4")
        self.checkBox_gpar_vision_res_addup = QtWidgets.QCheckBox(self.groupBox_gpar_pic)
        self.checkBox_gpar_vision_res_addup.setGeometry(QtCore.QRect(10, 160, 181, 16))
        self.checkBox_gpar_vision_res_addup.setChecked(True)
        self.checkBox_gpar_vision_res_addup.setObjectName("checkBox_gpar_vision_res_addup")
        self.lineEdit_gpar_vision_coef1 = QtWidgets.QLineEdit(self.groupBox_gpar_pic)
        self.lineEdit_gpar_vision_coef1.setEnabled(True)
        self.lineEdit_gpar_vision_coef1.setGeometry(QtCore.QRect(240, 30, 41, 20))
        self.lineEdit_gpar_vision_coef1.setObjectName("lineEdit_gpar_vision_coef1")
        self.label_gpar_vision_c1 = QtWidgets.QLabel(self.groupBox_gpar_pic)
        self.label_gpar_vision_c1.setGeometry(QtCore.QRect(180, 30, 71, 21))
        self.label_gpar_vision_c1.setObjectName("label_gpar_vision_c1")
        self.lineEdit_gpar_vision_coef2 = QtWidgets.QLineEdit(self.groupBox_gpar_pic)
        self.lineEdit_gpar_vision_coef2.setEnabled(True)
        self.lineEdit_gpar_vision_coef2.setGeometry(QtCore.QRect(240, 60, 41, 20))
        self.lineEdit_gpar_vision_coef2.setObjectName("lineEdit_gpar_vision_coef2")
        self.label_gpar_vision_c2 = QtWidgets.QLabel(self.groupBox_gpar_pic)
        self.label_gpar_vision_c2.setGeometry(QtCore.QRect(180, 60, 71, 21))
        self.label_gpar_vision_c2.setObjectName("label_gpar_vision_c2")
        self.label_gpar_vision_c3 = QtWidgets.QLabel(self.groupBox_gpar_pic)
        self.label_gpar_vision_c3.setGeometry(QtCore.QRect(180, 90, 71, 21))
        self.label_gpar_vision_c3.setObjectName("label_gpar_vision_c3")
        self.lineEdit_gpar_vision_coef3 = QtWidgets.QLineEdit(self.groupBox_gpar_pic)
        self.lineEdit_gpar_vision_coef3.setEnabled(True)
        self.lineEdit_gpar_vision_coef3.setGeometry(QtCore.QRect(240, 90, 41, 20))
        self.lineEdit_gpar_vision_coef3.setObjectName("lineEdit_gpar_vision_coef3")
        self.lineEdit_gpar_vision_coef4 = QtWidgets.QLineEdit(self.groupBox_gpar_pic)
        self.lineEdit_gpar_vision_coef4.setEnabled(True)
        self.lineEdit_gpar_vision_coef4.setGeometry(QtCore.QRect(240, 120, 41, 20))
        self.lineEdit_gpar_vision_coef4.setObjectName("lineEdit_gpar_vision_coef4")
        self.label_gpar_vision_c4 = QtWidgets.QLabel(self.groupBox_gpar_pic)
        self.label_gpar_vision_c4.setGeometry(QtCore.QRect(180, 120, 71, 21))
        self.label_gpar_vision_c4.setObjectName("label_gpar_vision_c4")
        self.groupBox_eng = QtWidgets.QGroupBox(cebsGparForm)
        self.groupBox_eng.setGeometry(QtCore.QRect(20, 400, 471, 251))
        self.groupBox_eng.setObjectName("groupBox_eng")
        self.textEdit_gpar_cmd_log = QtWidgets.QTextEdit(self.groupBox_eng)
        self.textEdit_gpar_cmd_log.setGeometry(QtCore.QRect(10, 20, 451, 161))
        self.textEdit_gpar_cmd_log.setMouseTracking(True)
        self.textEdit_gpar_cmd_log.setTabletTracking(True)
        self.textEdit_gpar_cmd_log.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_gpar_cmd_log.setAutoFillBackground(True)
        self.textEdit_gpar_cmd_log.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit_gpar_cmd_log.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_gpar_cmd_log.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textEdit_gpar_cmd_log.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.textEdit_gpar_cmd_log.setTabChangesFocus(True)
        self.textEdit_gpar_cmd_log.setObjectName("textEdit_gpar_cmd_log")
        self.pushButton_eng_clear = QtWidgets.QPushButton(self.groupBox_eng)
        self.pushButton_eng_clear.setGeometry(QtCore.QRect(80, 190, 81, 41))
        self.pushButton_eng_clear.setObjectName("pushButton_eng_clear")
        self.pushButton_gpar_pic_classify = QtWidgets.QPushButton(self.groupBox_eng)
        self.pushButton_gpar_pic_classify.setGeometry(QtCore.QRect(180, 190, 81, 41))
        self.pushButton_gpar_pic_classify.setObjectName("pushButton_gpar_pic_classify")
        self.pushButton_ctrl_giveup = QtWidgets.QPushButton(self.groupBox_eng)
        self.pushButton_ctrl_giveup.setGeometry(QtCore.QRect(280, 190, 81, 41))
        self.pushButton_ctrl_giveup.setObjectName("pushButton_ctrl_giveup")
        self.pushButton_ctrl_compl = QtWidgets.QPushButton(self.groupBox_eng)
        self.pushButton_ctrl_compl.setGeometry(QtCore.QRect(380, 190, 81, 41))
        self.pushButton_ctrl_compl.setObjectName("pushButton_ctrl_compl")
        self.groupBox_gpar_video = QtWidgets.QGroupBox(cebsGparForm)
        self.groupBox_gpar_video.setGeometry(QtCore.QRect(20, 200, 161, 191))
        self.groupBox_gpar_video.setObjectName("groupBox_gpar_video")
        self.lineEdit_gpar_video_input = QtWidgets.QLineEdit(self.groupBox_gpar_video)
        self.lineEdit_gpar_video_input.setGeometry(QtCore.QRect(80, 50, 51, 20))
        self.lineEdit_gpar_video_input.setObjectName("lineEdit_gpar_video_input")
        self.label_gpar_video_len = QtWidgets.QLabel(self.groupBox_gpar_video)
        self.label_gpar_video_len.setGeometry(QtCore.QRect(10, 50, 61, 21))
        self.label_gpar_video_len.setObjectName("label_gpar_video_len")
        self.checkBox_gpar_video_enable = QtWidgets.QCheckBox(self.groupBox_gpar_video)
        self.checkBox_gpar_video_enable.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.checkBox_gpar_video_enable.setCheckable(True)
        self.checkBox_gpar_video_enable.setChecked(False)
        self.checkBox_gpar_video_enable.setObjectName("checkBox_gpar_video_enable")
        self.label_gpar_video_sec = QtWidgets.QLabel(self.groupBox_gpar_video)
        self.label_gpar_video_sec.setGeometry(QtCore.QRect(140, 50, 41, 21))
        self.label_gpar_video_sec.setObjectName("label_gpar_video_sec")
        self.groupBox_gpar_bts = QtWidgets.QGroupBox(cebsGparForm)
        self.groupBox_gpar_bts.setGeometry(QtCore.QRect(20, 20, 471, 51))
        self.groupBox_gpar_bts.setObjectName("groupBox_gpar_bts")
        self.radioButton_gpar_bts_96 = QtWidgets.QRadioButton(self.groupBox_gpar_bts)
        self.radioButton_gpar_bts_96.setGeometry(QtCore.QRect(10, 20, 61, 21))
        self.radioButton_gpar_bts_96.setChecked(True)
        self.radioButton_gpar_bts_96.setObjectName("radioButton_gpar_bts_96")
        self.radioButton_gpar_bts_48 = QtWidgets.QRadioButton(self.groupBox_gpar_bts)
        self.radioButton_gpar_bts_48.setGeometry(QtCore.QRect(100, 20, 61, 21))
        self.radioButton_gpar_bts_48.setChecked(False)
        self.radioButton_gpar_bts_48.setObjectName("radioButton_gpar_bts_48")
        self.radioButton_gpar_bts_24 = QtWidgets.QRadioButton(self.groupBox_gpar_bts)
        self.radioButton_gpar_bts_24.setGeometry(QtCore.QRect(200, 20, 61, 21))
        self.radioButton_gpar_bts_24.setChecked(False)
        self.radioButton_gpar_bts_24.setObjectName("radioButton_gpar_bts_24")
        self.radioButton_gpar_bts_12 = QtWidgets.QRadioButton(self.groupBox_gpar_bts)
        self.radioButton_gpar_bts_12.setGeometry(QtCore.QRect(300, 20, 61, 21))
        self.radioButton_gpar_bts_12.setChecked(False)
        self.radioButton_gpar_bts_12.setObjectName("radioButton_gpar_bts_12")
        self.radioButton_gpar_bts_6 = QtWidgets.QRadioButton(self.groupBox_gpar_bts)
        self.radioButton_gpar_bts_6.setGeometry(QtCore.QRect(400, 20, 61, 21))
        self.radioButton_gpar_bts_6.setChecked(False)
        self.radioButton_gpar_bts_6.setObjectName("radioButton_gpar_bts_6")
        self.groupBox_gpar_pic_origin = QtWidgets.QGroupBox(cebsGparForm)
        self.groupBox_gpar_pic_origin.setGeometry(QtCore.QRect(510, 50, 651, 331))
        self.groupBox_gpar_pic_origin.setObjectName("groupBox_gpar_pic_origin")
        self.label_gpar_pic_origin_fill = QtWidgets.QLabel(self.groupBox_gpar_pic_origin)
        self.label_gpar_pic_origin_fill.setGeometry(QtCore.QRect(0, 20, 651, 311))
        self.label_gpar_pic_origin_fill.setObjectName("label_gpar_pic_origin_fill")
        self.groupBox_gpar_pic_cfy = QtWidgets.QGroupBox(cebsGparForm)
        self.groupBox_gpar_pic_cfy.setGeometry(QtCore.QRect(510, 390, 741, 521))
        self.groupBox_gpar_pic_cfy.setObjectName("groupBox_gpar_pic_cfy")
        self.label_gpar_pic_cfy_fill = QtWidgets.QLabel(self.groupBox_gpar_pic_cfy)
        self.label_gpar_pic_cfy_fill.setGeometry(QtCore.QRect(0, 20, 731, 491))
        self.label_gpar_pic_cfy_fill.setObjectName("label_gpar_pic_cfy_fill")
        self.pushButton_gpar_pic_file_load = QtWidgets.QPushButton(cebsGparForm)
        self.pushButton_gpar_pic_file_load.setGeometry(QtCore.QRect(1070, 20, 91, 21))
        self.pushButton_gpar_pic_file_load.setObjectName("pushButton_gpar_pic_file_load")
        self.lineEdit_gpar_pic_file_load = QtWidgets.QLineEdit(cebsGparForm)
        self.lineEdit_gpar_pic_file_load.setEnabled(True)
        self.lineEdit_gpar_pic_file_load.setGeometry(QtCore.QRect(580, 20, 471, 20))
        self.lineEdit_gpar_pic_file_load.setObjectName("lineEdit_gpar_pic_file_load")
        self.label_gpar_pic_file_load = QtWidgets.QLabel(cebsGparForm)
        self.label_gpar_pic_file_load.setGeometry(QtCore.QRect(510, 20, 51, 16))
        self.label_gpar_pic_file_load.setObjectName("label_gpar_pic_file_load")
        self.groupBox_eng_2 = QtWidgets.QGroupBox(cebsGparForm)
        self.groupBox_eng_2.setGeometry(QtCore.QRect(20, 670, 471, 141))
        self.groupBox_eng_2.setObjectName("groupBox_eng_2")
        self.pushButton_eng_clear_2 = QtWidgets.QPushButton(self.groupBox_eng_2)
        self.pushButton_eng_clear_2.setGeometry(QtCore.QRect(250, 30, 111, 91))
        self.pushButton_eng_clear_2.setObjectName("pushButton_eng_clear_2")
        self.pushButton_eng_clear_3 = QtWidgets.QPushButton(self.groupBox_eng_2)
        self.pushButton_eng_clear_3.setGeometry(QtCore.QRect(370, 30, 81, 41))
        self.pushButton_eng_clear_3.setObjectName("pushButton_eng_clear_3")
        self.pushButton_eng_clear_4 = QtWidgets.QPushButton(self.groupBox_eng_2)
        self.pushButton_eng_clear_4.setGeometry(QtCore.QRect(370, 80, 81, 41))
        self.pushButton_eng_clear_4.setObjectName("pushButton_eng_clear_4")

        self.retranslateUi(cebsGparForm)
        self.pushButton_ctrl_compl.clicked.connect(cebsGparForm.slot_gpar_compl)
        self.pushButton_ctrl_giveup.clicked.connect(cebsGparForm.slot_gpar_giveup)
        self.pushButton_gpar_pic_classify.clicked.connect(cebsGparForm.slot_gpar_pic_train)
        self.pushButton_gpar_pic_file_load.clicked.connect(cebsGparForm.slot_gpar_pic_file_load)
        self.pushButton_eng_clear.clicked.connect(cebsGparForm.slot_gpar_clear)
        self.pushButton_eng_clear_2.clicked.connect(cebsGparForm.slot_gpar_flu_cell_cnt)
        QtCore.QMetaObject.connectSlotsByName(cebsGparForm)

    def retranslateUi(self, cebsGparForm):
        _translate = QtCore.QCoreApplication.translate
        cebsGparForm.setWindowTitle(_translate("cebsGparForm", "工参配置"))
        self.groupBox_gpar_normal.setTitle(_translate("cebsGparForm", "全局参数设置"))
        self.checkBox_gpar_autoIdf.setText(_translate("cebsGparForm", "拍照后自动识别"))
        self.lineEdit_gpar_picTti.setText(_translate("cebsGparForm", "60"))
        self.label_gpar_picTti_title.setText(_translate("cebsGparForm", "定时拍照间隔"))
        self.label_gpar_picTti_min.setText(_translate("cebsGparForm", "分钟"))
        self.checkBox_gpar_autoPic.setText(_translate("cebsGparForm", "定时自动拍照"))
        self.checkBox_gpar_picFixPos.setText(_translate("cebsGparForm", "定点拍照"))
        self.groupBox_gpar_pic.setTitle(_translate("cebsGparForm", "图像识别参数设置"))
        self.lineEdit_gpar_vision_small_low_limit.setText(_translate("cebsGparForm", "200"))
        self.label_gpar_vision_t1.setText(_translate("cebsGparForm", "小尺寸门限"))
        self.lineEdit_gpar_vision_small_mid_limit.setText(_translate("cebsGparForm", "500"))
        self.label_gpar_vision_t2.setText(_translate("cebsGparForm", "小-中尺寸门限"))
        self.lineEdit_gpar_vision_mid_big_limit.setText(_translate("cebsGparForm", "2000"))
        self.label_gpar_vision_t3.setText(_translate("cebsGparForm", "中-大尺寸门限"))
        self.lineEdit_gpar_vision_big_upper_limit.setText(_translate("cebsGparForm", "5000"))
        self.label_gpar_vision_t4.setText(_translate("cebsGparForm", "大尺寸门限"))
        self.checkBox_gpar_vision_res_addup.setText(_translate("cebsGparForm", "输出图像叠加标定"))
        self.lineEdit_gpar_vision_coef1.setText(_translate("cebsGparForm", "5"))
        self.label_gpar_vision_c1.setText(_translate("cebsGparForm", "通用参数1"))
        self.lineEdit_gpar_vision_coef2.setText(_translate("cebsGparForm", "5"))
        self.label_gpar_vision_c2.setText(_translate("cebsGparForm", "通用参数2"))
        self.label_gpar_vision_c3.setText(_translate("cebsGparForm", "通用参数3"))
        self.lineEdit_gpar_vision_coef3.setText(_translate("cebsGparForm", "5"))
        self.lineEdit_gpar_vision_coef4.setText(_translate("cebsGparForm", "5"))
        self.label_gpar_vision_c4.setText(_translate("cebsGparForm", "通用参数4"))
        self.groupBox_eng.setTitle(_translate("cebsGparForm", "命令信息"))
        self.textEdit_gpar_cmd_log.setHtml(_translate("cebsGparForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TRACE LOG</p></body></html>"))
        self.pushButton_eng_clear.setText(_translate("cebsGparForm", "命令清除"))
        self.pushButton_gpar_pic_classify.setText(_translate("cebsGparForm", "图像训练"))
        self.pushButton_ctrl_giveup.setText(_translate("cebsGparForm", "设定放弃"))
        self.pushButton_ctrl_compl.setText(_translate("cebsGparForm", "设定完成"))
        self.groupBox_gpar_video.setTitle(_translate("cebsGparForm", "视频参数设置"))
        self.lineEdit_gpar_video_input.setText(_translate("cebsGparForm", "3"))
        self.label_gpar_video_len.setText(_translate("cebsGparForm", "视频时长"))
        self.checkBox_gpar_video_enable.setText(_translate("cebsGparForm", "开启视频记录"))
        self.label_gpar_video_sec.setText(_translate("cebsGparForm", "秒"))
        self.groupBox_gpar_bts.setTitle(_translate("cebsGparForm", "板型选择"))
        self.radioButton_gpar_bts_96.setText(_translate("cebsGparForm", "96孔板"))
        self.radioButton_gpar_bts_48.setText(_translate("cebsGparForm", "48孔板"))
        self.radioButton_gpar_bts_24.setText(_translate("cebsGparForm", "24孔板"))
        self.radioButton_gpar_bts_12.setText(_translate("cebsGparForm", "12孔板"))
        self.radioButton_gpar_bts_6.setText(_translate("cebsGparForm", "6孔板"))
        self.groupBox_gpar_pic_origin.setTitle(_translate("cebsGparForm", "原始图像"))
        self.label_gpar_pic_origin_fill.setText(_translate("cebsGparForm", "TextLabel"))
        self.groupBox_gpar_pic_cfy.setTitle(_translate("cebsGparForm", "识别后图像"))
        self.label_gpar_pic_cfy_fill.setText(_translate("cebsGparForm", "TextLabel"))
        self.pushButton_gpar_pic_file_load.setText(_translate("cebsGparForm", "文件导入"))
        self.label_gpar_pic_file_load.setText(_translate("cebsGparForm", "图像文件"))
        self.groupBox_eng_2.setTitle(_translate("cebsGparForm", "荧光细胞图像训练"))
        self.pushButton_eng_clear_2.setText(_translate("cebsGparForm", "荧光细胞计数"))
        self.pushButton_eng_clear_3.setText(_translate("cebsGparForm", "前一张"))
        self.pushButton_eng_clear_4.setText(_translate("cebsGparForm", "后一张"))

