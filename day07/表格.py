import xlrd
wb=xlrd.open_workbook(filename=r"D:\Users\lxx\Desktop\python\day07\day07\任务\2020年每个月的销售情况.xlsx",encoding_override=True)


shop={}
for i in range (12):
    st=wb.sheet_by_index(i)
    rows =st.nrows
    clos = st.ncols
    for row in range(1, rows):
        for clo in range(0, clos):
            s=st.cell_value(row, 1)
            p = st.cell_value(row,4)
            if s not in shop:
                shop[s]={
                    "销售量":p,
                    "单价": st.cell_value(row, 2)
                }
            elif s in shop:
                shop[s]={
                    "销售量":shop[s]["销售量"]+p,
                    "单价":st.cell_value(row,2)
                }
            break
print(shop)
qq=0.0 #全年销售额
mm=0.0#全年销售量
for i in shop:
    qq=qq+float(shop[i]["销售量"])*float(shop[i]["单价"])
    mm=mm+shop[i]["销售量"]
print("全年的销售总额：",qq,"元")
for i in shop:
    aa=(shop[i]["销售量"] /mm)*100
    nn=shop[i]["销售量"]*shop[i]["单价"]/qq*100
    print(i,"的销售占比：",'%.2f'% aa,"%")
    print(i,"的销售额占比：",'%.2f'% nn, "%")


max=shop["羽绒服"]["销售量"]
for i in shop:
    if max<shop[i]["销售量"]:
        max=shop[i]["销售量"]
        v=i
print("最畅销的衣服是:",v)

min=shop["羽绒服"]["销售量"]
for i in shop:
    if min>shop[i]["销售量"]:
        min=shop[i]["销售量"]
        v=i
print("全年销量最低的衣服:",v)

