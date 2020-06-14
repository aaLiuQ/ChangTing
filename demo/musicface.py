# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musicface.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(882, 654)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon/resizeApi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(0.9)  # 设置窗口透明度
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        self.widget = QtWidgets.QWidget(Form)
        # self.widget.setSpacing(0)
        self.widget.setGeometry(QtCore.QRect(160, 0, 721, 661))
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet('''
            QWidget#widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton{
            border:none;
            color:gray;
            font-size:12px;
            height:40px;
            padding-left:5px;
            padding-right:10px;
            text-align:left;
        }
        QPushButton:hover{
            color:black;
            border:1px solid #F3F3F5;
            border-radius:10px;
            background:LightGray;
        }
        ''')
        self.layoutWidget_3 = QtWidgets.QWidget(self.widget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(20, 120, 711, 391))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.pushButton_119 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_119.setObjectName("pushButton_119")
        self.horizontalLayout_32.addWidget(self.pushButton_119)
        self.pushButton_120 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_120.setObjectName("pushButton_120")
        self.horizontalLayout_32.addWidget(self.pushButton_120)
        self.pushButton_121 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_121.setObjectName("pushButton_121")
        self.horizontalLayout_32.addWidget(self.pushButton_121)
        self.pushButton_122 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_122.setObjectName("pushButton_122")

        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("./icon/dian.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_122.setIcon(icon10)

        self.horizontalLayout_32.addWidget(self.pushButton_122)
        self.verticalLayout_4.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.pushButton_123 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_123.setObjectName("pushButton_123")
        self.horizontalLayout_33.addWidget(self.pushButton_123)
        self.pushButton_124 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_124.setObjectName("pushButton_124")
        self.horizontalLayout_33.addWidget(self.pushButton_124)
        self.pushButton_125 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_125.setObjectName("pushButton_125")
        self.horizontalLayout_33.addWidget(self.pushButton_125)
        self.pushButton_126 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_126.setObjectName("pushButton_126")

        self.pushButton_126.setIcon(icon10)

        self.horizontalLayout_33.addWidget(self.pushButton_126)
        self.verticalLayout_4.addLayout(self.horizontalLayout_33)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.pushButton_127 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_127.setObjectName("pushButton_127")
        self.horizontalLayout_34.addWidget(self.pushButton_127)
        self.pushButton_128 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_128.setObjectName("pushButton_128")
        self.horizontalLayout_34.addWidget(self.pushButton_128)
        self.pushButton_129 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_129.setObjectName("pushButton_129")
        self.horizontalLayout_34.addWidget(self.pushButton_129)
        self.pushButton_130 = QtWidgets.QPushButton(self.layoutWidget_3)

        self.pushButton_130.setIcon(icon10)
        self.pushButton_130.setObjectName("pushButton_130")
        self.horizontalLayout_34.addWidget(self.pushButton_130)
        self.verticalLayout_4.addLayout(self.horizontalLayout_34)
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.pushButton_131 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_131.setObjectName("pushButton_131")
        self.horizontalLayout_35.addWidget(self.pushButton_131)
        self.pushButton_132 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_132.setObjectName("pushButton_132")
        self.horizontalLayout_35.addWidget(self.pushButton_132)
        self.pushButton_133 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_133.setObjectName("pushButton_133")
        self.horizontalLayout_35.addWidget(self.pushButton_133)
        self.pushButton_134 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_134.setIcon(icon10)
        self.pushButton_134.setObjectName("pushButton_134")
        self.horizontalLayout_35.addWidget(self.pushButton_134)
        self.verticalLayout_4.addLayout(self.horizontalLayout_35)
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.pushButton_135 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_135.setObjectName("pushButton_135")
        self.horizontalLayout_36.addWidget(self.pushButton_135)
        self.pushButton_136 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_136.setObjectName("pushButton_136")
        self.horizontalLayout_36.addWidget(self.pushButton_136)
        self.pushButton_137 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_137.setObjectName("pushButton_137")
        self.horizontalLayout_36.addWidget(self.pushButton_137)
        self.pushButton_138 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_138.setObjectName("pushButton_138")
        self.pushButton_138.setIcon(icon10)
        self.horizontalLayout_36.addWidget(self.pushButton_138)
        self.verticalLayout_4.addLayout(self.horizontalLayout_36)
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.pushButton_139 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_139.setObjectName("pushButton_139")
        self.horizontalLayout_37.addWidget(self.pushButton_139)
        self.pushButton_140 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_140.setObjectName("pushButton_140")
        self.horizontalLayout_37.addWidget(self.pushButton_140)
        self.pushButton_141 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_141.setObjectName("pushButton_141")
        self.horizontalLayout_37.addWidget(self.pushButton_141)
        self.pushButton_142 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_142.setIcon(icon10)
        self.pushButton_142.setObjectName("pushButton_142")
        self.horizontalLayout_37.addWidget(self.pushButton_142)
        self.verticalLayout_4.addLayout(self.horizontalLayout_37)
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.pushButton_143 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_143.setObjectName("pushButton_143")
        self.horizontalLayout_38.addWidget(self.pushButton_143)
        self.pushButton_144 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_144.setObjectName("pushButton_144")
        self.horizontalLayout_38.addWidget(self.pushButton_144)
        self.pushButton_145 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_145.setObjectName("pushButton_145")
        self.horizontalLayout_38.addWidget(self.pushButton_145)
        self.pushButton_146 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_146.setIcon(icon10)
        self.pushButton_146.setObjectName("pushButton_146")
        self.horizontalLayout_38.addWidget(self.pushButton_146)
        self.verticalLayout_4.addLayout(self.horizontalLayout_38)
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.pushButton_147 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_147.setObjectName("pushButton_147")
        self.horizontalLayout_39.addWidget(self.pushButton_147)
        self.pushButton_148 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_148.setObjectName("pushButton_148")
        self.horizontalLayout_39.addWidget(self.pushButton_148)
        self.pushButton_149 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_149.setObjectName("pushButton_149")
        self.horizontalLayout_39.addWidget(self.pushButton_149)
        self.pushButton_150 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_150.setIcon(icon10)
        self.pushButton_150.setObjectName("pushButton_150")
        self.horizontalLayout_39.addWidget(self.pushButton_150)
        self.verticalLayout_4.addLayout(self.horizontalLayout_39)
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.pushButton_151 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_151.setObjectName("pushButton_151")
        self.horizontalLayout_40.addWidget(self.pushButton_151)
        self.pushButton_152 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_152.setObjectName("pushButton_152")
        self.horizontalLayout_40.addWidget(self.pushButton_152)
        self.pushButton_153 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_153.setObjectName("pushButton_153")
        self.horizontalLayout_40.addWidget(self.pushButton_153)
        self.pushButton_154 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_154.setIcon(icon10)
        self.pushButton_154.setObjectName("pushButton_154")
        self.horizontalLayout_40.addWidget(self.pushButton_154)
        self.verticalLayout_4.addLayout(self.horizontalLayout_40)
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.pushButton_155 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_155.setObjectName("pushButton_155")
        self.horizontalLayout_41.addWidget(self.pushButton_155)
        self.pushButton_156 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_156.setObjectName("pushButton_156")
        self.horizontalLayout_41.addWidget(self.pushButton_156)
        self.pushButton_157 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_157.setObjectName("pushButton_157")
        self.horizontalLayout_41.addWidget(self.pushButton_157)
        self.pushButton_158 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_158.setIcon(icon10)
        self.pushButton_158.setObjectName("pushButton_158")
        self.horizontalLayout_41.addWidget(self.pushButton_158)
        self.verticalLayout_4.addLayout(self.horizontalLayout_41)
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(360, 600, 239, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.pushButton_167 = QtWidgets.QPushButton(self.widget)
        self.pushButton_167.setGeometry(QtCore.QRect(290, 620, 31, 23))
        self.pushButton_167.setObjectName("pushButton_167")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icon/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_167.setIcon(icon2)

        self.pushButton_168 = QtWidgets.QPushButton(self.widget)
        self.pushButton_168.setGeometry(QtCore.QRect(420, 620, 31, 23))
        self.pushButton_168.setObjectName("pushButton_168")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./icon/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_168.setIcon(icon3)

        self.pushButton_169 = QtWidgets.QPushButton(self.widget)
        self.pushButton_169.setGeometry(QtCore.QRect(550, 620, 31, 23))
        self.pushButton_169.setObjectName("pushButton_169")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./icon/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_169.setIcon(icon4)

        self.pushButton_170 = QtWidgets.QPushButton(self.widget)
        self.pushButton_170.setGeometry(QtCore.QRect(379, 510, 75, 21))
        self.pushButton_170.setObjectName("pushButton_170")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(145, 540, 450, 31))

        self.lineEdit_2.setPlaceholderText("Blueming")
        self.lineEdit_2.setObjectName("lineEdit")
        self.lineEdit_2.setStyleSheet(
            '''QLineEdit{
                    border:none; solid white;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(555, 510, 75, 21))
        self.lineEdit_3.setText("页数:")
        self.lineEdit_3.setObjectName("lineEdit")
        self.lineEdit_3.setStyleSheet(
            '''QLineEdit{
                    border:none; solid white;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')

        self.horizontalSlider = QtWidgets.QSlider(self.widget)
        self.horizontalSlider.setGeometry(QtCore.QRect(150, 580, 561, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setFixedHeight(3)

        self.label1 = QtWidgets.QLabel(self.widget)
        self.label1.setGeometry(QtCore.QRect(150, 600, 54, 12))
        self.label1.setObjectName("label")

        self.pushButton_171 = QtWidgets.QPushButton(self.widget)
        self.pushButton_171.setGeometry(QtCore.QRect(200, 510, 75, 21))
        self.pushButton_171.setObjectName("pushButton_171")
        self.layoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 100, 711, 20))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_45.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_45.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_45.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_45.addWidget(self.label_12)
        self.layoutWidget_4 = QtWidgets.QWidget(self.widget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(90, 50, 591, 22))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_46 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.radioButton_13 = QtWidgets.QRadioButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(10)
        self.radioButton_13.setFont(font)
        self.radioButton_13.setObjectName("radioButton_13")
        self.radioButton_13.setChecked(True)
        self.horizontalLayout_46.addWidget(self.radioButton_13)
        self.radioButton_14 = QtWidgets.QRadioButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(10)
        self.radioButton_14.setFont(font)
        self.radioButton_14.setObjectName("radioButton_14")
        self.horizontalLayout_46.addWidget(self.radioButton_14)
        self.radioButton_15 = QtWidgets.QRadioButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(10)
        self.radioButton_15.setFont(font)
        self.radioButton_15.setObjectName("radioButton_15")
        self.horizontalLayout_46.addWidget(self.radioButton_15)
        self.radioButton_16 = QtWidgets.QRadioButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(10)
        self.radioButton_16.setFont(font)
        self.radioButton_16.setObjectName("radioButton_16")
        self.horizontalLayout_46.addWidget(self.radioButton_16)
        self.radioButton_17 = QtWidgets.QRadioButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(10)
        self.radioButton_17.setFont(font)
        self.radioButton_17.setObjectName("radioButton_17")
        self.horizontalLayout_46.addWidget(self.radioButton_17)
        self.radioButton_18 = QtWidgets.QRadioButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(10)
        self.radioButton_18.setFont(font)
        self.radioButton_18.setObjectName("radioButton_18")
        self.horizontalLayout_46.addWidget(self.radioButton_18)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 20, 561, 21))
        self.lineEdit.setPlaceholderText("输入歌手、歌曲或用户，回车进行搜索")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(20, 550, 121, 100))

        self.frame.setStyleSheet("background-image:url(\"./icon/uir.jpg\")")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.pushButton_16 = QtWidgets.QPushButton(self.widget)
        self.pushButton_16.setGeometry(QtCore.QRect(20, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_16.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icon/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_16.setIcon(icon1)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.setStyleSheet('''
                border:none;
                        font-size:12px;
                        font-weight:700;
                        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                ''')
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 161, 661))
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
            QWidget#widget_2{
            background:gray;
            border-top:1px solid white;
            border-bottom:1px solid white;
            border-left:1px solid white;
            border-top-left-radius:10px;
            border-bottom-left-radius:10px;
        }
        ''')
        self.layoutWidget_5 = QtWidgets.QWidget(self.widget_2)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 40, 151, 571))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout.addWidget(self.pushButton_10)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_9)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_15 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout.addWidget(self.pushButton_15)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout.addWidget(self.pushButton_11)
        self.pushButton_14 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout.addWidget(self.pushButton_14)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout.addWidget(self.pushButton_13)
        self.layoutWidget_6 = QtWidgets.QWidget(self.widget_2)
        self.layoutWidget_6.setGeometry(QtCore.QRect(10, 20, 151, 25))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget_6)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFixedSize(15, 15)
        self.pushButton.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.pushButton.clicked.connect(QCoreApplication.quit)

        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget_6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setFixedSize(15, 15)
        self.pushButton_2.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget_6)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setFixedSize(15, 15)
        self.pushButton_3.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.pushButton_3.clicked.connect(Form.showMinimized)
        self.horizontalLayout.addWidget(self.pushButton_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ChangTing"))
        self.pushButton_119.setText(_translate("Form", ""))
        self.pushButton_120.setText(_translate("Form", ""))
        self.pushButton_121.setText(_translate("Form", ""))
        self.pushButton_122.setText(_translate("Form", ""))

        self.pushButton_123.setText(_translate("Form", ""))
        self.pushButton_124.setText(_translate("Form", ""))
        self.pushButton_125.setText(_translate("Form", ""))
        self.pushButton_126.setText(_translate("Form", ""))
        self.pushButton_127.setText(_translate("Form", ""))
        self.pushButton_128.setText(_translate("Form", ""))
        self.pushButton_129.setText(_translate("Form", ""))
        self.pushButton_130.setText(_translate("Form", ""))
        self.pushButton_131.setText(_translate("Form", ""))
        self.pushButton_132.setText(_translate("Form", ""))
        self.pushButton_133.setText(_translate("Form", ""))
        self.pushButton_134.setText(_translate("Form", ""))
        self.pushButton_135.setText(_translate("Form", ""))
        self.pushButton_136.setText(_translate("Form", ""))
        self.pushButton_137.setText(_translate("Form", ""))
        self.pushButton_138.setText(_translate("Form", ""))
        self.pushButton_139.setText(_translate("Form", ""))
        self.pushButton_140.setText(_translate("Form", ""))
        self.pushButton_141.setText(_translate("Form", ""))
        self.pushButton_142.setText(_translate("Form", ""))
        self.pushButton_143.setText(_translate("Form", ""))
        self.pushButton_144.setText(_translate("Form", ""))
        self.pushButton_145.setText(_translate("Form", ""))
        self.pushButton_146.setText(_translate("Form", ""))
        self.pushButton_147.setText(_translate("Form", ""))
        self.pushButton_148.setText(_translate("Form", ""))
        self.pushButton_149.setText(_translate("Form", ""))
        self.pushButton_150.setText(_translate("Form", ""))
        self.pushButton_151.setText(_translate("Form", ""))
        self.pushButton_152.setText(_translate("Form", ""))
        self.pushButton_153.setText(_translate("Form", ""))
        self.pushButton_154.setText(_translate("Form", ""))
        self.pushButton_155.setText(_translate("Form", ""))
        self.pushButton_156.setText(_translate("Form", ""))
        self.pushButton_157.setText(_translate("Form", ""))
        self.pushButton_158.setText(_translate("Form", ""))

        self.pushButton_167.setText(_translate("Form", ""))
        self.pushButton_168.setText(_translate("Form", ""))
        self.pushButton_169.setText(_translate("Form", ""))
        self.pushButton_170.setText(_translate("Form", "下一页"))
        self.pushButton_171.setText(_translate("Form", "上一页"))
        self.label1.setText(_translate("Form", "00:00"))
        self.label_9.setText(_translate("Form", "歌手"))
        self.label_10.setText(_translate("Form", "歌曲名"))
        self.label_11.setText(_translate("Form", "平台"))
        self.label_12.setText(_translate("Form", "操作"))
        self.radioButton_13.setText(_translate("Form", "网易云"))
        self.radioButton_14.setText(_translate("Form", "QQ音乐"))
        self.radioButton_15.setText(_translate("Form", "酷狗音乐"))
        self.radioButton_16.setText(_translate("Form", "酷我音乐"))
        self.radioButton_17.setText(_translate("Form", "喜马拉雅"))
        self.radioButton_18.setText(_translate("Form", "全民K歌"))
        self.pushButton_16.setText(_translate("Form", "搜索"))
        self.pushButton_4.setText(_translate("Form", "每日推荐"))
        self.pushButton_5.setText(_translate("Form", "华语流行"))
        self.pushButton_6.setText(_translate("Form", "在线FM"))
        self.pushButton_10.setText(_translate("Form", "热门MV"))
        self.pushButton_9.setText(_translate("Form", "我的音乐"))
        self.pushButton_7.setText(_translate("Form", "本地音乐"))
        self.pushButton_15.setText(_translate("Form", "下载管理"))
        self.pushButton_8.setText(_translate("Form", "我的收藏"))
        self.pushButton_11.setText(_translate("Form", "联系与帮助"))
        self.pushButton_14.setText(_translate("Form", "反馈意见"))
        self.pushButton_12.setText(_translate("Form", "关注我们"))
        self.pushButton_13.setText(_translate("Form", "遇到问题"))
        self.pushButton.setText(_translate("Form", ""))
        self.pushButton_2.setText(_translate("Form", ""))
        self.pushButton_3.setText(_translate("Form", ""))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
