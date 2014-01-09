# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GelberZettel.ui'
#
# Created: Sun Jan  5 00:32:14 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import GuiOverwrites

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        #self.Maintab = QtGui.QTabWidget(self.centralwidget)
        self.Maintab = GuiOverwrites.MyTabWidget(self.centralwidget)
        self.Maintab.setObjectName("Maintab")
        self.verticalLayout.addWidget(self.Maintab)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Maintab.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Zettel", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setToolTip(QtGui.QApplication.translate("MainWindow", "Left Mouse Button Double Click to add tab \n"
" Right Mouse Button Double Click to remove active tab", None, QtGui.QApplication.UnicodeUTF8))

