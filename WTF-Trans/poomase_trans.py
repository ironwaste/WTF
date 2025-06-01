import pandas as pd
import datetime
import time
from PyQt5.QtCore import QDate

def trans_changci(changci,date) :
    # 输入格式 场次号 ‘A1001’ 和 字符串格式的日期 ‘2025-01-01’
    # 输出： 单场地号 A  、  场次号1001 、 以及 日期 2025/1/1
    # 转换场次号 和 场地
    s = str(changci)
    num = (int)(s[1]) - 1

    # 时间转换 datetimw 函数库 中日期运算的参考链接
    # https://blog.csdn.net/webcai_3/article/details/147158557 参考链接
    dt = datetime.datetime.strptime(date,"%Y-%m-%d")
    delta = datetime.timedelta(days=num)
    dt = dt + delta
    date_str = dt.strftime("%Y/%m/%d")
    # return s[0],s[1:5]
    # 将 A1001 拆分为 A 和 1001 两种  还有 场次号的第一位
    # 并且再增加一位用于判断当前场次，为赛事的第几天 第一天以0开始，0，1，2，3 形式表示。
    return s[0],s[1:5],date_str


def get_tableview_poomase(model , date):
    rows = model.rowCount()
    cols = model.columnCount()

    colunms = ['bisixuho','riqi','chngdi','chngci','cixu',
               'xingming','xingbie','fenlei','dnwei','zubie',
               'jibie','lunci','jingsixingmu1']
    data = []
    cnt = 2 # 用于标 比赛序号
    # 输出
    # 比赛序号（0）、日期（1）、场地（2）、场地号（3）、次序号（4）、姓名（5）
    # 性别（6）、分类（7）、单位（8）、组别（为空）（9）、级别（10），
    # 轮次（11）先为手动，因为不好判断轮次个数
    for row in range(rows) :
        row_data = [str(cnt),'','','','','','','','','','','1','']
        cnt += 1
        for col in range(cols) :
            item = model.item(row,col)
            if col == 0 :
                changdi,changdihao,tianshu = trans_changci(item.text(),date)
                row_data[2] = changdi
                row_data[3] = changdihao
                row_data[1] = tianshu
            elif col == 1:
                # 次序号 上场顺序
                row_data[4] = item.text()
            elif col == 2 :
                # 姓名 以及 分类
                cnt_name_str = item.text()
                row_data[5] = cnt_name_str
                start = 0
                number = 0
                fenlei = ['个人','混双','团品']
                # 分类 ： 个人、 混双、 团品
                # 通过查看 姓名单元格 的/斜杠的个数来判断是 个人（0个）、混双（1个）、团品（2个）
                while start != -1 :
                    start = cnt_name_str.find('/',start)
                    if start == -1 :
                        break
                    start += 1
                    number += 1
                row_data[7] = fenlei[number]
            elif col == 3 :
                # 性别
                row_data[6] = item.text()
            elif col == 4 :
                # 单位
                row_data[8] = item.text()
            elif col == 5 :
                # 级别
                row_data[10] = item.text()
            elif col == 6 :
                # lunci 先手动
                # 对应的是 row_data[11]
                continue
            elif col == 7 :
                str_name = str(item.text())
                row_data[12] = str_name[:-1]
        data.append(row_data)

    df = pd.DataFrame(data,columns=colunms)
    return df
