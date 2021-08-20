'''
跨地区转账利率1%
跨行转账利率5%
'''
from DBUtils import up_date
from DBUtils import select_date
info='''
------------个人信息----------------
账号：%s,
用户名：%s,
密码：******,
余额：%s,
账号类型：%s
地址信息：
    国家：%s,
    省份：%s,
    街道：%s,
    门牌号：%s,
开户行：%s
-----------------------------------
'''
def page():
    print("*************************************")
    print("*           中国农业银行              *")
    print("*           账户管理系统              *")
    print("*              V1.0                 *")
    print("*************************************")
    print("*1、开户                             *")
    print("*2、存钱                             *")
    print("*3、取钱                             *")
    print("*4、转账                             *")
    print("*5、查询                             *")
    print("*6、Bye!                            *")
    print("*"*37)

account=["33333333","44444444"]
user ={"中国农业银行":[{"账号":"33333333","账号类型":"一类账户","姓名":"赵四","密码":"333333","存款":0},{"账号":"44444444","账号类型":"二类账户","姓名":"王五","密码":"444444","存款":1000}]}
usersity={"33333333":[{"国家":"中国","省份":"北京市","街道":"昌平","门牌号":"301"}],"44444444":[{"国家":"中国","省份":"河南","街道":"郑州","门牌号":"302"}]}

#开户
def addname():
    import random
    str = ""
    for i in range(8):
        card=chr(random.randrange(ord("0"), ord("9") - 1))
        str=str +card
    chose_card=input("请输入账号类型：")
    name=input("请输入您的姓名：")
    key=input("请输入账户密码：")
    country = input("请输入国家：")
    province = input("请输入省份：")
    street = input("请输入街道：")
    house = input("请输入门牌号：")
    money=int(input("请输入初始存入金额："))
    brank = "中国农业银行"
    sql="select * from user2"
    date=select_date(sql,[])
    if len(date)>100:
        print("银行账户已满！")
        return 3
    else:
        sql1="select * from user2 where 账号 = %s"
        param1=[str]
        date1=select_date(sql1,param1)
        if len(date1)==0:
            sql2 = "insert into user2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            param2=[str,name,key,money,chose_card,country,province,street,house]
            up_date(sql2,param2)
            print("开户成功！以下是您的开户信息：")
            print(info % (str,name,country,province,street,house,money,chose_card,brank))
            return 1
        else:
            print("账号已存在！")
            return 2

#存钱
def save_money():
    brankcard=input("请输入您的账户：")
    sql1 = "select * from user2 where 账号 = %s"
    param1 = [brankcard]
    date1 = select_date(sql1, param1)
    if len(date1) > 0:
        deposit = float(input("请输入需要存入的金额："))
        sql2 = "UPDATE user2 SET 存款 = 存款 + %s WHERE 账号 = %s"
        param2 = [deposit, brankcard]
        up_date(sql2, param2)
        print("存款成功！")
        aa = "select 存款 from user2 where 账号 = %s"
        bb = select_date(aa, brankcard)
        print("账号余额为：", bb[0][0])
        return True
    else:
        print("账户不存在！")
        return False

#取钱
def get_money():
    brankcard = input("请输入您的账户：")
    sql1 = "select * from user2 where 账号 = %s"
    param1 = [brankcard]
    date1 = select_date(sql1, param1)
    if len(date1) > 0:
        pwd = input("请输入账户密码：")
        if pwd==date1[0][2]:
            deposit = float(input("请输入需要取出的金额："))
            if deposit<=date1[0][3]:
                sql2 = "UPDATE user2 SET 存款 = 存款 - %s WHERE 账号 = %s"
                param2 = [deposit, brankcard]
                up_date(sql2, param2)
                print("取款成功！")
                aa = "select 存款 from user2 where 账号 = %s"
                bb = select_date(aa, brankcard)
                print("账号余额为：", bb[0][0])
            else:
                print("账户余额不足！")
                return 3
        else:
            print("账号密码错误！")
            return 2
    else:
        print("账户不存在！")
        return 1

#跨行转账
def take_money(card,deposit):
    sql1 = "select * from user2 where 账号 = %s"
    param1 = [card]
    date1 = select_date(sql1, param1)
    if len(date1) > 0:
        sql2 = "UPDATE user2 SET 存款 = 存款 + %s WHERE 账号 = %s"
        param2 = [deposit, card]
        up_date(sql2, param2)
        return 1
    else:
        return 2


#转账
def make_money():
    out_card=input("请输入转出的银行账号：")
    up_card=input("请输入转入的银行账号：")
    sql1 = "select * from user2 where 账号 = %s"
    param1 = [out_card]
    date1 = select_date(sql1, param1)
    sql2 = "select * from user2 where 账号 = %s"
    param2 = [up_card]
    date2 = select_date(sql2, param2)
    if len(date1) > 0 and len(date2) > 0:
        pwd=input("请输入转出的银行账号密码：")
        if pwd==date1[0][2]:
            deposit = float(input("请输入转账的金额："))
            deposit_1=deposit*1.01
            if date1[0][4] == "一类账户" and deposit_1<=50000:
                if deposit_1 <= date1[0][3]:
                    if date1[0][6]==date2[0][6]:
                        sql3 = "UPDATE user2 SET 存款 = 存款 - %s WHERE 账号 = %s"
                        param3 = [deposit, out_card]
                        up_date(sql3, param3)
                        sql4 = "UPDATE user2 SET 存款 = 存款 + %s WHERE 账号 = %s"
                        param4 = [deposit, up_card]
                        up_date(sql4, param4)
                        print("转账成功！")
                        aa = "select 存款 from user2 where 账号 = %s"
                        bb = select_date(aa, out_card)
                        print("转出的账户余额为：", bb[0][0])
                        return True
                    else:
                        sql3 = "UPDATE user2 SET 存款 = 存款 - %s WHERE 账号 = %s"
                        param3 = [deposit_1, out_card]
                        up_date(sql3, param3)
                        sql4 = "UPDATE user2 SET 存款 = 存款 + %s WHERE 账号 = %s"
                        param4 = [deposit, up_card]
                        up_date(sql4, param4)
                        print("转账成功！")
                        aa = "select 存款 from user2 where 账号 = %s"
                        bb = select_date(aa, out_card)
                        print("转出的账户余额为：", bb[0][0])
                        return True
                else:
                    print("转出的银行账户余额不足！")
                    return 3
            elif date1[0][4]=="二类账户" and deposit_1 <= 20000:
                if deposit_1 <= date1[0][3]:
                    if date1[0][6] == date2[0][6]:
                        sql3 = "UPDATE user2 SET 存款 = 存款 - %s WHERE 账号 = %s"
                        param3 = [deposit, out_card]
                        up_date(sql3, param3)
                        sql4 = "UPDATE user2 SET 存款 = 存款 + %s WHERE 账号 = %s"
                        param4 = [deposit, up_card]
                        up_date(sql4, param4)
                        print("转账成功！")
                        aa = "select 存款 from user2 where 账号 = %s"
                        bb = select_date(aa, out_card)
                        print("转出的账户余额为：", bb[0][0])
                        return True
                    else:
                        sql3 = "UPDATE user2 SET 存款 = 存款 - %s WHERE 账号 = %s"
                        param3 = [deposit_1, out_card]
                        up_date(sql3, param3)
                        sql4 = "UPDATE user2 SET 存款 = 存款 + %s WHERE 账号 = %s"
                        param4 = [deposit, up_card]
                        up_date(sql4, param4)
                        print("转账成功！")
                        aa = "select 存款 from user2 where 账号 = %s"
                        bb = select_date(aa, out_card)
                        print("转出的账户余额为：", bb[0][0])
                        return True
                else:
                    print("转出的银行账户余额不足！")
                    return 3
            else:
                print("银行账号额度不足！")
        else:
            print("转出的银行账户密码错误！")
            return 2
    else:
        if len(date1) > 0:
            pwd = input("请输入转出的银行账号密码：")
            if pwd == date1[0][2]:
                deposit = float(input("请输入转账的金额："))
                deposit_1 = deposit * 1.05
                if date1[0][4] == "一类账户" and deposit_1 <= 50000:
                    if deposit_1 <= date1[0][3]:
                        from 中国工商银行_date import take_money
                        s=take_money(up_card, deposit)
                        if s==1:
                            sql5 = "UPDATE user2 SET 存款 = 存款 - %s WHERE 账号 = %s"
                            param5 = [deposit_1, out_card]
                            up_date(sql5, param5)
                            print("转账成功！")
                            aa = "select 存款 from user2 where 账号 = %s"
                            bb = select_date(aa, out_card)
                            print("转出的账户余额为：", bb[0][0])
                            return True
                        elif s==2:
                            print("账号不存在")
                            return False
                    else:
                        print("转出的银行账户余额不足！")
                        return 3
                elif date1[0][4] == "二类账户" and deposit_1 <= 20000:
                    if deposit_1 <= date1[0][3]:
                        from 中国工商银行_date import take_money
                        s=take_money(up_card, deposit)
                        if s==1:
                            sql5 = "UPDATE user2 SET 存款 = 存款 - %s WHERE 账号 = %s"
                            param5 = [deposit_1, out_card]
                            up_date(sql5, param5)
                            print("转账成功！")
                            aa = "select 存款 from user2 where 账号 = %s"
                            bb = select_date(aa, out_card)
                            print("转出的账户余额为：", bb[0][0])
                            return True
                        elif s==2:
                            print("账号不存在")
                            return False
                    else:
                        print("转出的银行账户余额不足！")
                        return 3
                else:
                    print("银行账号额度不足！")
            else:
                print("转出的银行账户密码错误！")
                return 2
        else:
            print("账号不存在！")
            return 1

#查询
def look_user():
    brankcard = input("请输入查询的账号：")
    sql1 = "select * from user2 where 账号 = %s"
    param1 = [brankcard]
    date1 = select_date(sql1, param1)
    if len(date1) > 0:
        pwd = input("请输入账号密码：")
        if pwd==date1[0][2]:
                print(info % (date1[0][0],date1[0][1],date1[0][3],date1[0][4],date1[0][5],date1[0][6],date1[0][7],date1[0][8],"中国农业银行"))
        else:
            print("银行账号密码错误！")
    else:
        print("该用户不存在！")


def interface():
    while True:
        page()
        choose = int(input("请选择需要办理的业务:"))
        if choose ==1:
            addname()
        elif choose ==2:
            save_money()
        elif choose ==3:
            get_money()
        elif choose ==4:
            make_money()
        elif choose ==5:
            look_user()
        elif choose==6:
            print("Bye!")
            break
        else:
            print("请正确输入要办理的业务！")
# interface()

if __name__ == '__main__':
    interface()