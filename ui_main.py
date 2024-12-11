# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QTableView,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(686, 654)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(80, 20, 581, 151))
        self.Update_pushButton = QPushButton(self.centralwidget)
        self.Update_pushButton.setObjectName(u"Update_pushButton")
        self.Update_pushButton.setGeometry(QRect(80, 190, 75, 24))
        self.Name_lineEdit = QLineEdit(self.centralwidget)
        self.Name_lineEdit.setObjectName(u"Name_lineEdit")
        self.Name_lineEdit.setGeometry(QRect(80, 270, 113, 22))
        self.Price_spinBox = QSpinBox(self.centralwidget)
        self.Price_spinBox.setObjectName(u"Price_spinBox")
        self.Price_spinBox.setGeometry(QRect(220, 270, 91, 22))
        self.Description_textEdit = QTextEdit(self.centralwidget)
        self.Description_textEdit.setObjectName(u"Description_textEdit")
        self.Description_textEdit.setGeometry(QRect(340, 270, 104, 71))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 250, 61, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 250, 61, 16))
        self.label_2.setStyleSheet(u"*{\n"
"color:rgb(255, 170, 255)}")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 250, 61, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(470, 250, 61, 16))
        self.Category_comboBox = QComboBox(self.centralwidget)
        self.Category_comboBox.setObjectName(u"Category_comboBox")
        self.Category_comboBox.setGeometry(QRect(470, 270, 69, 22))
        self.Add_pushButton = QPushButton(self.centralwidget)
        self.Add_pushButton.setObjectName(u"Add_pushButton")
        self.Add_pushButton.setGeometry(QRect(210, 370, 231, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 686, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Update_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.Add_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

