import face
import fighttrans
import poomase_trans

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QDate
import numpy as np
import time
import xlsxwriter

class T(face.Ui_widget,QtWidgets.QWidget) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.my_label("正在修改文件中，请稍后")

        # 将日历设置为当前日期
        ## 获取当前时间
        self.year = (int)(time.strftime("%Y"))
        self.month = (int)(time.strftime("%m"))
        self.day = (int)(time.strftime("%d"))
        self.date = QDate(self.year, self.month, self.day)
        self.calendarWidget.setSelectedDate(self.date)
        # 结束

        self.fight_import_button.clicked.connect(self.get_openfile_path)
        self.fight_output_buttom.clicked.connect(self.trans_fight)

        self.poomsae_import_button.clicked.connect(self.get_openfile_path)
        self.poomsae_import_button_2.clicked.connect(self.get_openfile_path)

        self.poomsae_output_button.clicked.connect(self.trans_poomsae)

    def trans_poomsae(self):
        self.getDate()
        self.df_out_poomase = poomase_trans.get_tableview_poomase(self.model,self.selectDate)
        self.df_out_poomase['riqi'] = pd.to_datetime(self.df_out_poomase['riqi']).dt.date
        self.out_filename = f'{self.selectDate}_品势_{self.event_name}'
        with pd.ExcelWriter(f'{self.out_filename}.xlsx', engine='xlsxwriter') as writer:
            # 将 DataFrame 写入 Excel
            self.df_out_poomase.to_excel(writer, sheet_name=self.event_name, index=False)
            print(f'self.event_name:{self.event_name}')
            # 获取工作簿和工作表对象
            workbook = writer.book
            worksheet = writer.sheets[self.event_name]

            # 定义 yyyy/m/d 日期格式
            date_format = workbook.add_format({'date_format': 14})

            # 设置日期列的格式（根据列索引）
            # 假设日期列为：order_date (C列), delivery_date (D列), timestamp (E列), mixed_date (F列)
            date_columns = {'B': 'riqi'}

            # 应用日期格式到指定列
            for col_letter, col_name in date_columns.items():
                col_idx = ord(col_letter) - 65  # 将列字母转换为索引（A=0, B=1, C=2...）
                # 设置整列格式（从第1行开始，跳过标题行）
                worksheet.set_column(col_idx, col_idx, 15, date_format)

        self.my_label(f"品势修改完成：文件名称为{self.out_filename}.xlsx")

    def trans_fight(self) :
        self.getDate()
        self.df_out_fight = fighttrans.get_tabelview_fight(self.model,self.selectDate)
        self.out_filename = f"{self.selectDate}_竞技_{self.event_name}"

        self.df_out_fight.to_excel(f'{self.out_filename}.xlsx',index=False,sheet_name=self.event_name)
        self.my_label("修改完成！")


    def format_date(date):
        # 用于品势日期转换
        """将日期格式化为 yyyy/m/d 字符串"""
        if pd.isna(date):
            return ""
        return f"{date.year}/{date.month}/{date.day}"

    def get_openfile_path(self) :  # 文件选择
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'Excel files(*.xlsx , *.xls)')
        self.filename = openfile_name[0]
        if self.filename == '' : # 如果未选择文件，则显示重新选择
            self.my_label("文件未被选择，请重新选择")
        else : # 否则将显示 文件内容
            self.my_label("文件已经导入,内容如右表")
            tmp_df = pd.read_excel(self.filename) # 文件导入
            self.event_name = tmp_df.columns.tolist()[0]
            self.data_pretreat(tmp_df)
            # 数据预处理 将赛事名称 和 内容分离
            self.init_tabel_view()


    def data_pretreat(self,df): # 将赛事名称 和 内容和数据进行分离
        df = df.replace(np.nan,'')
        df.columns = df.loc[0]
        self.df = df.loc[1:]
        # return name,df

    def my_label(self,string) :
        self.output_label.setText(str(string))

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
                else :
                    item = QStandardItem(str(value))
                item.setTextAlignment(Qt.AlignCenter) # 将文本项居中显示
                self.model.setItem(row,col,item)
        self.tableView.setModel(self.model)

    def getDate(self) :
        # calendarWidget to get selected date 获取当前选中日期
        self.selectDate = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")


if __name__ == '__main__' :
    app = QtWidgets.QApplication(sys.argv)
    win = T()
    win.show()
    sys.exit(app.exec())
