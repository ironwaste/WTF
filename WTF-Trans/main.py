from PyQt5 import QtCore, QtGui, QtWidgets
import face
import fighttrans
import sys
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QDate
import numpy as np
import time

class T(face.Ui_widget,QtWidgets.QWidget) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.start_label()

        # 将日历设置为当前日期
        ## 获取当前时间
        year = (int)(time.strftime("%Y"))
        month = (int)(time.strftime("%m"))
        day = (int)(time.strftime("%d"))
        date = QDate(year, month, day)
        self.calendarWidget.setSelectedDate(date)
        # 结束

        self.fight_import_button.clicked.connect(self.get_openfile_path)
        self.poomsae_import_button.clicked.connect(self.get_openfile_path)
        self.poomsae_import_button_2.clicked.connect(self.get_openfile_path)
        self.fight_output_buttom.clicked.connect(self.trans_fight)

    def getDate(self) :
        # calendarWidget to get selected date and to 判断场次为赛事第几天从而得到最后日期
        self.selectDate = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        # print(self.selectDate)

    def trans_fight(self) :
        self.getDate()
        self.df_out_fight = fighttrans.get_tabelview_fight(self.model,self.selectDate)
        # print(self.df_out_fight)
        # print(self.df_out_fight.head())
        self.df_out_fight.to_excel('output.xlsx',index=False)
        self.my_label("修改完成！")


    def init_tabel_view(self) : # 显示在 tabelview中并且 列宽根据内容进行调整
        self.model = QStandardItemModel()
        rows,cols = self.df.shape
        self.model.setRowCount(rows)
        self.model.setColumnCount(cols)
        list = self.df.columns.tolist()
        self.model.setHorizontalHeaderLabels(list)

        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)  # 自动适应内容
        # header.setSectionResizeMode(QHeaderView.Stretch)        # 所有列平均拉伸填充视图

        for row in range(rows) :
            for col in range(cols) :
                value = self.df.iat[row,col]
                if pd.isna(value) :
                    item = QStandardItemModel('')
                else:
                    item = QStandardItem(str(value))
                item.setTextAlignment(Qt.AlignCenter) # 将文本项居中显示
                self.model.setItem(row,col,item)
        self.tableView.setModel(self.model)


    def get_openfile_path(self) :  # 文件选择
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'Excel files(*.xlsx , *.xls)')
        self.filename = openfile_name[0]

        if self.filename == '' : # 如果未选择文件，则显示重新选择
            self.my_label("文件未被选择，请重新选择")
        else : # 否则将显示 文件内容

            self.my_label("文件已经导入,内容如右表")
            tmp_df = pd.read_excel(self.filename) # 文件导入

            self.event_name,self.df = self.data_pretreat(tmp_df)
            # 数据预处理 将赛事名称 和 内容分离
            # print(self.df)
            self.init_tabel_view()



    def data_pretreat(self,df): # 将赛事名称 和 内容和数据进行分离

        df = df.replace(np.nan,'')
        df.columns = df.loc[0]
        name = df.columns.tolist()[0]
        df = df.loc[1:]
        return name,df

    def start_label(self) :
        self.output_label.setText("请选择输入文件")

    def change_label(self):
        self.output_label.setText("正在修改文件中，请稍后")

    def my_label(self,string) :
        self.output_label.setText(str(string))

if __name__ == '__main__' :
    app = QtWidgets.QApplication(sys.argv)
    win = T()
    win.show()
    sys.exit(app.exec())
