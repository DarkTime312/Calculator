# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Calculator_dark.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resource_rc

class Ui_CalculatorDarkView(object):
    def setupUi(self, CalculatorDarkView):
        if not CalculatorDarkView.objectName():
            CalculatorDarkView.setObjectName(u"CalculatorDarkView")
        CalculatorDarkView.resize(400, 700)
        CalculatorDarkView.setMinimumSize(QSize(400, 700))
        CalculatorDarkView.setMaximumSize(QSize(400, 700))
        icon = QIcon()
        icon.addFile(u":/Assets/empty.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        CalculatorDarkView.setWindowIcon(icon)
        CalculatorDarkView.setStyleSheet(u"QWidget#CalculatorDarkView {\n"
"	background-color: black;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: 1px solid black;\n"
"	border-radius: 0;\n"
"}\n"
"\n"
"QLabel {\n"
"margin-right: 10px;\n"
"color: white\n"
"}\n"
"\n"
"/*  Operation buttons */\n"
"QPushButton#btn_divide,\n"
" QPushButton#btn_multiply,\n"
" QPushButton#btn_minus,\n"
" QPushButton#btn_plus,\n"
" QPushButton#btn_equal {\n"
"background-color: #FF9500;\n"
"color: white\n"
"}\n"
"\n"
"QPushButton#btn_divide:hover,\n"
" QPushButton#btn_multiply:hover,\n"
" QPushButton#btn_minus:hover,\n"
" QPushButton#btn_plus:hover,\n"
" QPushButton#btn_equal:hover {\n"
"background-color: #ffb143;\n"
"}\n"
"\n"
"QPushButton#btn_divide:pressed,\n"
" QPushButton#btn_multiply:pressed,\n"
" QPushButton#btn_minus:pressed,\n"
" QPushButton#btn_plus:pressed,\n"
" QPushButton#btn_equal:pressed {\n"
"background-color: #FF9500;\n"
"}\n"
"\n"
"/*  top buttons */\n"
"\n"
"QPushButton#btn_ac,\n"
" QPushButton#btn_change_sign,\n"
" QPushButton#btn_percent {\n"
"background-color"
                        ": #505050;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton#btn_ac:hover,\n"
" QPushButton#btn_change_sign:hover,\n"
" QPushButton#btn_percent:hover {\n"
"background-color: #686868;\n"
"}\n"
"\n"
"QPushButton#btn_ac:pressed,\n"
" QPushButton#btn_change_sign:pressed,\n"
" QPushButton#btn_percent:pressed {\n"
"background-color: #505050;\n"
"}\n"
"\n"
"/*  Number buttons */\n"
"\n"
"QPushButton#btn_0,\n"
"QPushButton#btn_1,\n"
" QPushButton#btn_2,\n"
" QPushButton#btn_3,\n"
" QPushButton#btn_4,\n"
"QPushButton#btn_5,\n"
"QPushButton#btn_6,\n"
" QPushButton#btn_7,\n"
" QPushButton#btn_8,\n"
" QPushButton#btn_9,\n"
" QPushButton#btn_dot{\n"
"background-color: #d4d4d2;\n"
"}\n"
"\n"
"QPushButton#btn_0:hover,\n"
"QPushButton#btn_1:hover,\n"
" QPushButton#btn_2:hover,\n"
" QPushButton#btn_3:hover,\n"
" QPushButton#btn_4:hover,\n"
"QPushButton#btn_5:hover,\n"
"QPushButton#btn_6:hover,\n"
" QPushButton#btn_7:hover,\n"
" QPushButton#btn_8:hover,\n"
" QPushButton#btn_9:hover,\n"
" QPushButton#btn_dot:hover{\n"
"background-col"
                        "or: #efefed;\n"
"}\n"
"\n"
"QPushButton#btn_0:pressed,\n"
"QPushButton#btn_1:pressed,\n"
" QPushButton#btn_2:pressed,\n"
" QPushButton#btn_3:pressed,\n"
" QPushButton#btn_4:pressed,\n"
"QPushButton#btn_5:pressed,\n"
"QPushButton#btn_6:pressed,\n"
" QPushButton#btn_7:pressed,\n"
" QPushButton#btn_8:pressed,\n"
" QPushButton#btn_9:pressed,\n"
" QPushButton#btn_dot:pressed{\n"
"background-color: #d4d4d2;\n"
"}\n"
"\n"
"/*  All buttons disabled */\n"
"\n"
"QPushButton#btn_0:disabled,\n"
"QPushButton#btn_1:disabled,\n"
" QPushButton#btn_2:disabled,\n"
" QPushButton#btn_3:disabled,\n"
" QPushButton#btn_4:disabled,\n"
"QPushButton#btn_5:disabled,\n"
"QPushButton#btn_6:disabled,\n"
" QPushButton#btn_7:disabled,\n"
" QPushButton#btn_8:disabled,\n"
" QPushButton#btn_9:disabled,\n"
" QPushButton#btn_dot:disabled,\n"
"QPushButton#btn_divide:disabled,\n"
" QPushButton#btn_multiply:disabled,\n"
" QPushButton#btn_minus:disabled,\n"
" QPushButton#btn_plus:disabled,\n"
" QPushButton#btn_equal:disabled,\n"
"QPushButton#btn_ac:d"
                        "isabled,\n"
" QPushButton#btn_change_sign:disabled,\n"
" QPushButton#btn_percent:disabled {\n"
"color: #999999;\n"
"}")
        self.verticalLayout = QVBoxLayout(CalculatorDarkView)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_small = QLabel(CalculatorDarkView)
        self.lbl_small.setObjectName(u"lbl_small")
        font = QFont()
        font.setFamilies([u"Helvetica"])
        font.setPointSize(25)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.lbl_small.setFont(font)
        self.lbl_small.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)
        self.lbl_small.setWordWrap(False)
        self.lbl_small.setMargin(0)
        self.lbl_small.setIndent(0)

        self.verticalLayout.addWidget(self.lbl_small)

        self.lbl_big = QLabel(CalculatorDarkView)
        self.lbl_big.setObjectName(u"lbl_big")
        font1 = QFont()
        font1.setFamilies([u"Helvetica"])
        font1.setPointSize(50)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.lbl_big.setFont(font1)
        self.lbl_big.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lbl_big.setMargin(0)
        self.lbl_big.setIndent(0)

        self.verticalLayout.addWidget(self.lbl_big)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.btn_1 = QPushButton(CalculatorDarkView)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Helvetica"])
        font2.setPointSize(25)
        font2.setBold(False)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.btn_1.setFont(font2)

        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_percent = QPushButton(CalculatorDarkView)
        self.btn_percent.setObjectName(u"btn_percent")
        sizePolicy.setHeightForWidth(self.btn_percent.sizePolicy().hasHeightForWidth())
        self.btn_percent.setSizePolicy(sizePolicy)
        self.btn_percent.setFont(font2)

        self.gridLayout.addWidget(self.btn_percent, 0, 2, 1, 1)

        self.btn_4 = QPushButton(CalculatorDarkView)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setFont(font2)

        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_ac = QPushButton(CalculatorDarkView)
        self.btn_ac.setObjectName(u"btn_ac")
        sizePolicy.setHeightForWidth(self.btn_ac.sizePolicy().hasHeightForWidth())
        self.btn_ac.setSizePolicy(sizePolicy)
        self.btn_ac.setFont(font2)

        self.gridLayout.addWidget(self.btn_ac, 0, 0, 1, 1)

        self.btn_change_sign = QPushButton(CalculatorDarkView)
        self.btn_change_sign.setObjectName(u"btn_change_sign")
        sizePolicy.setHeightForWidth(self.btn_change_sign.sizePolicy().hasHeightForWidth())
        self.btn_change_sign.setSizePolicy(sizePolicy)
        self.btn_change_sign.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u":/Assets/invert_light.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_change_sign.setIcon(icon1)
        self.btn_change_sign.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.btn_change_sign, 0, 1, 1, 1)

        self.btn_7 = QPushButton(CalculatorDarkView)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setFont(font2)

        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_divide = QPushButton(CalculatorDarkView)
        self.btn_divide.setObjectName(u"btn_divide")
        sizePolicy.setHeightForWidth(self.btn_divide.sizePolicy().hasHeightForWidth())
        self.btn_divide.setSizePolicy(sizePolicy)
        self.btn_divide.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/Assets/divide_light.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_divide.setIcon(icon2)
        self.btn_divide.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btn_divide, 0, 3, 1, 1)

        self.btn_8 = QPushButton(CalculatorDarkView)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setFont(font2)

        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_9 = QPushButton(CalculatorDarkView)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setFont(font2)

        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_multiply = QPushButton(CalculatorDarkView)
        self.btn_multiply.setObjectName(u"btn_multiply")
        sizePolicy.setHeightForWidth(self.btn_multiply.sizePolicy().hasHeightForWidth())
        self.btn_multiply.setSizePolicy(sizePolicy)
        self.btn_multiply.setFont(font2)

        self.gridLayout.addWidget(self.btn_multiply, 1, 3, 1, 1)

        self.btn_5 = QPushButton(CalculatorDarkView)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setFont(font2)

        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_6 = QPushButton(CalculatorDarkView)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setFont(font2)

        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_minus = QPushButton(CalculatorDarkView)
        self.btn_minus.setObjectName(u"btn_minus")
        sizePolicy.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy)
        self.btn_minus.setFont(font2)

        self.gridLayout.addWidget(self.btn_minus, 2, 3, 1, 1)

        self.btn_2 = QPushButton(CalculatorDarkView)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setFont(font2)

        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_3 = QPushButton(CalculatorDarkView)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setFont(font2)

        self.gridLayout.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_plus = QPushButton(CalculatorDarkView)
        self.btn_plus.setObjectName(u"btn_plus")
        sizePolicy.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy)
        self.btn_plus.setFont(font2)

        self.gridLayout.addWidget(self.btn_plus, 3, 3, 1, 1)

        self.btn_dot = QPushButton(CalculatorDarkView)
        self.btn_dot.setObjectName(u"btn_dot")
        sizePolicy.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy)
        self.btn_dot.setFont(font2)

        self.gridLayout.addWidget(self.btn_dot, 4, 2, 1, 1)

        self.btn_equal = QPushButton(CalculatorDarkView)
        self.btn_equal.setObjectName(u"btn_equal")
        sizePolicy.setHeightForWidth(self.btn_equal.sizePolicy().hasHeightForWidth())
        self.btn_equal.setSizePolicy(sizePolicy)
        self.btn_equal.setFont(font2)

        self.gridLayout.addWidget(self.btn_equal, 4, 3, 1, 1)

        self.btn_0 = QPushButton(CalculatorDarkView)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setFont(font2)

        self.gridLayout.addWidget(self.btn_0, 4, 0, 1, 2)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 5)

        self.retranslateUi(CalculatorDarkView)

        QMetaObject.connectSlotsByName(CalculatorDarkView)
    # setupUi

    def retranslateUi(self, CalculatorDarkView):
        CalculatorDarkView.setWindowTitle("")
        self.lbl_small.setText("")
        self.lbl_big.setText("")
        self.btn_1.setText(QCoreApplication.translate("CalculatorDarkView", u"1", None))
        self.btn_percent.setText(QCoreApplication.translate("CalculatorDarkView", u"%", None))
        self.btn_4.setText(QCoreApplication.translate("CalculatorDarkView", u"4", None))
        self.btn_ac.setText(QCoreApplication.translate("CalculatorDarkView", u"AC", None))
        self.btn_change_sign.setText("")
        self.btn_7.setText(QCoreApplication.translate("CalculatorDarkView", u"7", None))
        self.btn_divide.setText("")
        self.btn_8.setText(QCoreApplication.translate("CalculatorDarkView", u"8", None))
        self.btn_9.setText(QCoreApplication.translate("CalculatorDarkView", u"9", None))
        self.btn_multiply.setText(QCoreApplication.translate("CalculatorDarkView", u"x", None))
        self.btn_5.setText(QCoreApplication.translate("CalculatorDarkView", u"5", None))
        self.btn_6.setText(QCoreApplication.translate("CalculatorDarkView", u"6", None))
        self.btn_minus.setText(QCoreApplication.translate("CalculatorDarkView", u"-", None))
        self.btn_2.setText(QCoreApplication.translate("CalculatorDarkView", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("CalculatorDarkView", u"3", None))
        self.btn_plus.setText(QCoreApplication.translate("CalculatorDarkView", u"+", None))
        self.btn_dot.setText(QCoreApplication.translate("CalculatorDarkView", u".", None))
        self.btn_equal.setText(QCoreApplication.translate("CalculatorDarkView", u"=", None))
        self.btn_0.setText(QCoreApplication.translate("CalculatorDarkView", u"0", None))
    # retranslateUi

