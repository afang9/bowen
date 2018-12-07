import xlrd
class Read_Shuju():
    def duqu_shuju(self):
        shuju=[]
        f=xlrd.open_workbook(r'E:\py\kuangjia\data\北京.xlsx')
        sheet=f.nsheets
        sheet=f.sheets()[0]
        hang=sheet.nrows
        for i in range(1,hang):
            shuj=sheet.row_values(i)
            shuju.append(shuj)
        print(shuju)
        return shuju
    def wenjian(self):
        with open('实例.txt','r')as f:
            c=f.read().split('\n')
        return c
a=Read_Shuju()
a.duqu_shuju()
print(a.wenjian())