#/usr/bin/env python
#--*--conding utf-8 -*-
def sgwc(a,jine):
    while True:
        global zongjia
        c = input('购物车清理：ID,*,数量/结束请输‘end’：')
        c = c.split(',')
        if c == ['end']:
            if a<jine:
                print('总消费：', a)
                print('欢迎下次光临！')
                break
        elif int(c[0]) == 1:
            jiageyi = diannao['price']
            zongjia = jiageyi * int(c[2])
        elif int(c[0]) == 2:
            jiageer = shubiao['price']
            zongjia = jiageer * int(c[2])
        elif int(c[0]) == 3:
            jiagesan = youting['price']
            zongjia = jiagesan * int(c[2])
        elif int(c[0]) == 4:
            jiagesi = meinv['price']
            zongjia = jiagesi * int(c[2])
        else:
            print('序列号错误,请重新输入')
        a -= zongjia
        # else:
        print('总价为：', a)
        break
    return a

####################################################################################
if __name__=='__main__':      #不想被调用，写在这个下面（跨文件函数调用）
    a1=input('请输入金额:')
    jine=int(a1)
    diannao={'name':'电脑','price':1999,'ID':1}
    shubiao={'name':'鼠标','price':10,'ID':2}
    youting={'name':'游艇','price':20,'ID':3}
    meinv={'name':'美女','price':998,'ID':4}
    huodan=[diannao,shubiao,youting,meinv]
    for ii in range(4):
        print(huodan[ii])
    b=input('是否购买商品yes:')
    if b=='no':
        print('欢迎下次光临！')
    elif b=='yes':
        #global a
        a=0
        zongjia=0
        while True:
            a += zongjia
            print('总价为：', a)
            c=input('请输入商品序列号及数量(ID,*,数量)/结束请输‘end’：')
            c=c.split(',')
            if c==['end']:
                if a<jine:
                    print('总消费：', a)
                    print('欢迎下次光临！')
                    break
                elif a>jine:
                    while True:
                        print('总消费：',a)
                        cz=input('余额不足，请充值(退出：end/充值:输入金额/购物车清理：end2）')
                        if cz=='end':
                            break
                        elif cz=='end2':
                            sgwc(a,jine)
                            a=sgwc(a,jine)
                            zongjia = 0
                            break
                        else:
                            while True:
                                cz1=int(cz)
                                jine+=cz1
                                if jine>a:
                                    print('购买成功，欢迎下次光临！')
                                    break
                                else:
                                    break
                else:
                    break
            elif int(c[0] )== 1:
                jiageyi=diannao['price']
                zongjia=jiageyi*int(c[2])
            elif int(c[0])== 2:
                jiageer=shubiao['price']
                zongjia=jiageer*int(c[2])
            elif int(c[0])==3:
                jiagesan=youting['price']
                zongjia=jiagesan*int(c[2])
            elif int(c[0])==4:
                jiagesi=meinv['price']
                zongjia=jiagesi*int(c[2])
            else:
                print('序列号错误,请重新输入')