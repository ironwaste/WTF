# WTF
the format translate about  taekwondo compition





-----



任务记录 ：2025-5-17 将竞技对战表 除时间部分将所有的都已经进行完成。需增加 日历选择的和根据场地号判断当前的比赛日期。



## 竞技对战表 转换 前台表

### 输入格式

1. 场次 （而后可能空一行）

2. 轮次

3. 青方姓名

4. 代表队 （单位）

5. -VS-

6. 红方姓名

7. 代表队 （单位）

8. 级别

9. 备注

	

图片编辑网站（马赛克） ：https://www.fotor.com/cn/features/mosaics.html

输入格式 例子

![fight-input1](/markdown-img/fight-input1.png)

![fight-input2](/markdown-img/fight-input2.png)

![fight-input3](/markdown-img/fight-input3.png)



#### 竞技标准输入格式 : 

![fight-output](/markdown-img/竞技标准输入对阵表.jpg)



### 输出格式



输出的竞技对战表的格式（也就是目标转换格式）：

​	第一行标题行格式应如下 ，而第一列的比赛序号，是随便的只要是不同的就可以（主要是用于使用后面数据时的方便 猜测，具体代码实现未知）



​	文字格式 : Times New Roman ;Font size = 10;

![fight-output](/markdown-img/fight-output.png)

| bisaixuhao | zonglunci |     lunci      | changdi | changdihao   | jibie | gerentuanti | riqi | qingfangbianhao | qingfangxinming | qingfangdanwei | hongfangbianhao | hongfangxinming | hongfangdanwei |
| ---------- | --------- | :------------: | ------- | ------------ | ----- | ----------- | ---- | --------------- | --------------- | -------------- | --------------- | --------------- | -------------- |
| 数字       | 空NAN     | （c+数字）文本 | A、B、C | 1001（文本） | 文本  | 个人        | 文本 | 空 NAN          | 文本            | 文本           | 空 NAN          | 文本            | 文本           |

下方表格有部分是不需要的，所以也就没有什么所谓，上方表格基本是必须的，而序号数字也是必须的不管可以步从107987开始。

| bisaixuhao | zonglunci | lunci | changdi | changdihao | jibie | gerentuanti | riqi | qingfangbianhao | qingfangxinming | qingfangdanwei | hongfangbianhao | hongfangxinming | hongfangdanwei | bisaizhuangtai | huoshengzhe | huoshengfangshi | qingfangdefen | hongfangdefen | qingfangkoufen | hongfangkoufen | qingfangdefen1 | hongfangdefen1 | qingfangkoufen1 | hongfangkoufen1 | qingfangdefen2 | hongfangdefen2 | qingfangkoufen2 | hongfangkoufen2 | qingfangdefen3 | hongfangdefen3 | qingfangkoufen3 | hongfangkoufen3 | qingfangdefen4 | hongfangdefen4 | qingfangkoufen4 | hongfangkoufen4 | yijian | erjian | sanjian | qingwinnum | hongwinnum |
| ---------- | --------- | ----- | ------- | ---------- | ----- | ----------- | ---- | --------------- | --------------- | -------------- | --------------- | --------------- | -------------- | -------------- | ----------- | --------------- | ------------- | ------------- | -------------- | -------------- | -------------- | -------------- | --------------- | --------------- | -------------- | -------------- | --------------- | --------------- | -------------- | -------------- | --------------- | --------------- | -------------- | -------------- | --------------- | --------------- | ------ | ------ | ------- | ---------- | ---------- |
| 107987     |           |       |         |            |       |             |      |                 |                 |                |                 |                 |                |                |             |                 |               |               |                |                |                |                |                 |                 |                |                |                 |                 |                |                |                 |                 |                |                |                 |                 |        |        |         |            |            |
| 107988     |           |       |         |            |       |             |      |                 |                 |                |                 |                 |                |                |             |                 |               |               |                |                |                |                |                 |                 |                |                |                 |                 |                |                |                 |                 |                |                |                 |                 |        |        |         |            |            |
| 107989     |           |       |         |            |       |             |      |                 |                 |                |                 |                 |                |                |             |                 |               |               |                |                |                |                |                 |                 |                |                |                 |                 |                |                |                 |                 |                |                |                 |                 |        |        |         |            |            |



1. bisaixuhao （比赛序号，普通数字）
2. ~~zonglunci （最终轮次 为空）~~
3. lunci（轮次   格式一般为  c+数字  ）
4. changdi（场地 一般为A、B、C 等 大写英文字母）
5. chngdiho （场地号 一般为 1001 1002 1003 ）
6. jibie (级别 组别 一般为 ’男B组33kg‘ 等 )
7. gerentuanti （一般填写 个人或者团体）
8. riqi （日期 ： 一般可以直接填写当前时间的日期 ，不过格式一定需要是 ‘2024-4-4’ 文本）
9. ~~qingfangbianhao （青方编号 不填）~~
10. qingfangxingming （青方姓名 ）
11. qingfangdanwei （青方单位 ）
12. ~~hongfanbianhao（红方编号）不填~~
13. hongfangxingming（红方姓名）
14. hongfangdanwei（红方单位）















