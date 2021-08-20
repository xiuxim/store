import xlrd
import pymysql
wb=xlrd.open_workbook(filename=r"D:\Users\lxx\Desktop\python\day07\day07\任务\每月数据.xlsx",encoding_override=True)
con=pymysql.connect(host="localhost",user="root",password="",database="excel")
cursor=con.cursor()
v=0
excel=['1Jan','2Feb','3Mar','4Apr','5May','6Jun','7Jul','8Aug','9Sep','10Oct','11Nov','12Dec']
for i in excel:
    sql = "CREATE TABLE if not exists " + i + " (`日期` VARCHAR(10),`服装名称` VARCHAR(10),`价格/件` FLOAT,`本月库存数量` FLOAT,`销售量/每日` FLOAT)"
    print(sql)
    cursor.execute(sql)
    con.commit()
    st = wb.sheet_by_index(v)
    rows = st.nrows
    cols = st.ncols
    for row in range(1,rows):
        date = st.row_values(row)
        sql1 = "insert into " + i + " values (%s,%s,%s,%s,%s)"
        print(sql1)
        param1 = date
        cursor.execute(sql1, param1)
        con.commit()
    v = v+1
cursor.close()
con.close()



