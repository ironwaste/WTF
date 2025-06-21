import pandas as pd
import datetime

def trans_num(lunci) :
    # 转换 轮次 1/4 为 c4
    s = str(lunci)
    n = len(s)
    # print(n)
    out ='c'
    for i in range(2,n) : # 转换 1/ 之后的所有数字 有可能是两位或者多位数字的情况
        out += s[i]
    if s[0] != '1' :
        # 由于除了决赛是 final 字符串，其余都是分数格式且 分子为 1
        # 所以判断第一个值是为为一即可
        out = "c1"
    return str(out)  # 输出为 c + 数字 的文本格式

def trans_changci(changci) :
# 转换场次号 和 场地
    s = str(changci)
    num = (int)(s[1]) - 1
    # print(num)
    return s[0],s[1:5],num # 将 A1001 拆分为 A 和 1001 两种  还有 场次号的第一位
    # 并且再增加一位用于判断当前场次，为赛事的第几天 第一天以0开始，0，1，2，3 形式表示。



def trans_date(date,tianshu) :
# https://blog.csdn.net/webcai_3/article/details/147158557 参考链接
    dt = datetime.datetime.strptime(date,"%Y-%m-%d")
    delta = datetime.timedelta(days=tianshu)
    dt = dt + delta
    date = dt.strftime("%Y-%m-%d")
    return date

def get_tabelview_fight( model, date ):
    # 获取行列数量
    rows = model.rowCount()
    cols = model.columnCount()

    # 提取列名（水平表头）
    # 比赛序号、‘空’、轮次、场地、场地号、级别、个人团体、日期、青方姓名、
    columns = ['bisaixuhao','zonglunci','lunci','changdi','chngdiho','jibie',
               'gerentuanti','riqi','qingfangbianhao','qingfangxinming',
               'qingfangdanwei','hongfangbianhao','hongfangxinming',
               'hongfangdanwei']
    # 提取数据‘
    data = []
    cnt = 2
    for row in range(rows):

        row_data = [str(cnt),'','','','','','个人','','','','','','','']
        #
        cnt += 1
        for col in range(cols) :
            item = model.item(row, col)
            if col == 0 : # 判断场地
                changdi,changdihao,tianshu = trans_changci(str(item.text()))
                row_data[3] = changdi
                row_data[4] = str(changdihao)
                row_data[7] = trans_date(date,tianshu)
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
        data.append(row_data)

    # 创建 DataFrame
    df = pd.DataFrame(data, columns=columns)
    return df

