# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/vlados/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(372, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Trajectory_plot_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Trajectory_plot_btn.setGeometry(QtCore.QRect(10, 10, 351, 61))
        self.Trajectory_plot_btn.setObjectName("Trajectory_plot_btn")
        self.Moving_plot_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Moving_plot_btn.setGeometry(QtCore.QRect(10, 80, 351, 61))
        self.Moving_plot_btn.setObjectName("Moving_plot_btn")
        self.Velosity_plot_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Velosity_plot_btn.setGeometry(QtCore.QRect(10, 150, 351, 61))
        self.Velosity_plot_btn.setObjectName("Velosity_plot_btn")
        self.Axeleration_plot_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Axeleration_plot_btn.setGeometry(QtCore.QRect(10, 220, 351, 61))
        self.Axeleration_plot_btn.setObjectName("Axeleration_plot_btn")
        self.Close_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Close_btn.setGeometry(QtCore.QRect(10, 380, 351, 91))
        self.Close_btn.setAutoFillBackground(False)
        self.Close_btn.setObjectName("Close_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Trajectory_plot_btn.setText(_translate("MainWindow", "Manipulator moving"))
        self.Moving_plot_btn.setText(_translate("MainWindow", "Q(t)"))
        self.Velosity_plot_btn.setText(_translate("MainWindow", "Q\'(t)"))
        self.Axeleration_plot_btn.setText(_translate("MainWindow", "Q\'\'(t)"))
        self.Close_btn.setText(_translate("MainWindow", "Close"))

