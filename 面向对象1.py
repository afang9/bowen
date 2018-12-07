class ZhiHui():
    def zhishu(self):
        sum_zhishu=0
        for i in range(2,101):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                sum_zhishu+=i
        return sum_zhishu
    def huiwen(self,zfc):
        fzfc=zfc[::-1]
        if fzfc==zfc:
            print('%s'%('说明是回文'))
        else:
            print('%s'%('no'))

if __name__=='__main__':
    zhihui=ZhiHui()
    print(zhihui.zhishu())
    zhihui.huiwen('qweewq')

class Cat():
    def eat(self,):
        print('%s爱吃鱼'%('小猫'))
    def drink(self):
        print('%s爱喝水'%('小包'))

if __name__=='__main__':
    new_cat=Cat():
