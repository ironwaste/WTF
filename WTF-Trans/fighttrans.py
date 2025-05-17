from PyQt5 import QtGui, QtWidgets, QtCore
import openpyxl as oxl
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, Qt
import face


def trans_num(lunci) :
    # 转换 轮次 1/4 为 c4
    s = str(lunci)
    n = len(s)
    # print(n)
    out ='c'
    for i in range(2,n) : # 转换 1/ 之后的所有数字 有可能是两位或者多位数字的情况
        out += s[i]
    if s[0] != '1' :
        out = "c1"
    return str(out)  # 输出为 c + 数字 的文本格式

def trans_changci(changci) :
# 转换场次号 和 场地
    s = str(changci)
    num = float(s[1])
    return s[0],s[1:5],num # 将 A1001 拆分为 A 和 1001 两种  还有 场次号的第一位
    # 并且再增加一位用于判断当前场次，为赛事的第几天 第一天以0开始，0，1，2，3 形式表示。




# def trans_date(date) :
# 未完成，不知道 calendarywidget 最后所获取的 日期的格式 是什么样子的


def get_tabelview_fight( model, date ):

    # 获取行列数量
    rows = model.rowCount()
    cols = model.columnCount()
    print(rows)
    print(cols)

    # 提取列名（水平表头）
    columns = ['bisaixuhao','zonglunci','lunci','changdi','chngdiho','jibie',
               'gerentuanti','riqi','qingfangbianhao','qingfangxinming',
               'qingfangdanwei','hongfangbianhao','hongfangxinming',
               'hongfangdanwei']
    # 提取数据‘
    data = []
    cnt = 2
    for row in range(rows):

        row_data = [str(cnt),'','','','','','个人','','','','','','','']
        cnt += 1
        for col in range(cols) :
            item = model.item(row, col)
            if col == 0 :
                changdi,changdihao,tianshu = trans_changci(str(item.text()))
                row_data[3] = changdi
                row_data[4] = str(changdihao)
                # list[7] = time + tianshu  日期时间 还未完成
            elif col == 1 :
                continue
            elif col == 2 :
                lunci = trans_num(str(item.text()))
                row_data[2] = str(lunci)
            elif col == 3 :
                row_data[9] = str(item.text())
            elif col == 4 :
                row_data[10] = str(item.text())
            elif col == 6 :
                row_data[12] = str(item.text())
            elif col == 7 :
                row_data[13] = str(item.text())
            elif col == 8 :
                row_data[5] = str(item.text())
        print(row_data)
        data.append(row_data)

    # 创建 DataFrame
    df = pd.DataFrame(data, columns=columns)
    return df


