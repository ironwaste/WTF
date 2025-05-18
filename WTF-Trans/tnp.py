import pandas as pd
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import Qt
import pandas as pd
import numpy as np
import datetime

# date_str = "2025-5-18"
#
#
# # ttributeError: module 'datetime' has no attribute 'strptime' 错误，
# # 通常是因为错误地调用了 datetime 模块中的方法。
# # strptime 方法属于 datetime 类（datetime 模块中的一个子类）
# # 而非直接属于 datetime 模块本身。
# dt = datetime.datetime.strptime("2025-5-18","%Y-%m-%d")
# print(dt)


# list = [1,2,3,4,4,5]
#
# list[1] = str(0)
# print(list)



# # 创建应用实例（必须）
# app = QApplication([])
#
# # 示例DataFrame
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'Score': [89.5, 92.3, 78.9]
# }
# df = pd.DataFrame(data)
#
# # 初始化模型和视图
# model = QStandardItemModel()
# view = QTableView()
#
# # 设置模型行列数
# rows, cols = df.shape
# model.setRowCount(rows)
# model.setColumnCount(cols)
#
# # 设置水平表头（列名）
# model.setHorizontalHeaderLabels(df.columns.tolist())
#
# # 填充数据
# for row in range(rows):
#     for col in range(cols):
#         value = df.iat[row, col]  # 使用iat快速访问标量值
#         # 处理NaN或None，转换为空字符串
#         if pd.isna(value):
#             item = QStandardItem('')
#         else:
#             item = QStandardItem(str(value))
#         # 可选：设置数值右对齐
#         if isinstance(value, (int, float)):
#             item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
#         model.setItem(row, col, item)
#
# # 将模型设置到视图并显示
# view.setModel(model)
# view.setWindowTitle("DataFrame in Qt View")
# view.resize(600, 400)
# view.show()
#
# # 执行应用
# app.exec_()