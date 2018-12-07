#/usr/bin/env python
#--*-- coding:utf-8 -*-
a=int(input('请输入金额：'))
goods=  [{'name':'电脑','price':1999},
        {'name':'鼠标','price':10},
        {'name':'游艇','price':20},
        {'name':'美女','price':998}]
for i,j in enumerate(goods):
        print(i+1,j['name'],j['price'])
s=0
d=[]
while True:
        e=int(input('请根据商品序号来购买:1-电脑;2-鼠标;3-游艇;4-美女;5-exit(退出):::'))
        if e<5:
                c=goods[e-1]['price']
                d.append(e)
                s+=c
                print('总消费: {}'.format(s))
        elif e==5:
                print('请去结账:')
                break
print(d)
# while True:
if a<s:
        print('请充值或者删除购物车,如果想移除购物车,请选择对应的想移除的商品:')
        r=int(input('请选择移除的商品序号,输入6-delete: 输入9充值'))
        if r==6:
                for k in d:
                        t=int(input('请根据商品序号来移除:1-电脑;2-鼠标;3-游艇;4-美女;5-exit(退出):::'))
                        if k==t:
                                d.remove(t)
                                print(d)
                        elif t==5:
                                continue
        elif r==9:
                while True:
                        y=int(input('请选择充值金额'))
                        a+=y
                        print('充值成功,余额为: {}'.format(a))
                        if a>s:
                                a-=s
                                print('购买成功,余额为: {}'.format(a))
                                break







