from PyQt5 import QtCore, QtGui, QtWidgets
import openpyxl as oxl

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate,Qt


def import_sheet(path):
    workBook = oxl.load_workbook(path)
    sheet = workBook.active
    return sheet



class Ui_MainWindow(QtWidgets.QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(491, 393)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.retranslateUi(MainWindow)


        self.fightImport = QtWidgets.QPushButton(self.centralWidget)
        self.fightImport.setGeometry(QtCore.QRect(10, 160, 150, 120)) # 10,160,131,101
        self.fightImport.setObjectName("fightImport")

        self.playImport = QtWidgets.QPushButton(self.centralWidget)
        self.playImport.setGeometry(QtCore.QRect(330, 160, 131, 101))
        self.playImport.setObjectName("playImport")

        self.fightImport.setText("竞技对阵表导入并且导出")

        self.playImport.setText("品势对阵表导入")
        MainWindow.setCentralWidget(self.centralWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        # 绑定事件 fight import
        self.fightImport.clicked.connect(self.openfile)


        #绑定事件 perfrom import
        self.playImport.clicked.connect(self.openfile)


    def retranslateUi(self, MainWindow):
        # _translate = QtCore.QCoreApplication.translate
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "跆拳道客户端对阵表转换"))


    def openfile(self):
        openfile_name = QFileDialog.getOpenFileName(self,'选择文件','','Excel files(*.xlsx , *.xls)')
        list =[]
        list.append(openfile_name[0])
        # sheet = import_sheet(list[0])
        # write_execl(sheet)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
