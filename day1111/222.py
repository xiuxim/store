import xlrd
import pymysql
# con=pymysql.connect(host="localhost",user="root",password="",database="bank")
# cursor=con.cursor()
# sql="select 姓名 from user"
# param=[]
# cursor.execute(sql,param)
#
# date=cursor.fetchall()
#
# print(date)
# cursor.close()
# con.close()
# sql="select * from user1"
# date=select_date(sql,[])
# print(date[1])
# con=pymysql.connect(host="localhost",user="root",password="",database="excel")
# cursor=con.cursor()
#
# excel=['1Jan','2Feb','3Mar','4Apr','5May','6Jun','7Jul','8Aug','9Sep','10Oct','11Nov','12Dec']
# for i in excel:
#     sql = "CREATE TABLE " + i + " (`日期` VARCHAR(10),`服装名称` VARCHAR(10),`价格/件` FLOAT,`本月库存数量` INT,`销售量/每日` INT)"
#     sq = sql
#     cursor.execute(sq)
#     con.commit()
# cursor.close()
# con.close()
wb=xlrd.open_workbook(filename=r"D:\Users\lxx\Desktop\python\day07\day07\任务\每月数据.xlsx",encoding_override=True)
v=0
excel=['1Jan','2Feb','3Mar','4Apr','5May','6Jun','7Jul','8Aug','9Sep','10Oct','11Nov','12Dec']
for i in excel:
    print(i)
    st = wb.sheet_by_index(v)
    rows = st.nrows
    cols = st.ncols
    for row in range(1, rows):
        date = st.row_values(row)
        print(date)
    v=v+1
