import xlrd
from APP框架.config.Music_定域 import Login
def read_shuju():
    f=xlrd.open_workbook(r'E:\py\APP框架\data\登录.xlsx')
    sheet=f.nsheets
    sheet=f.sheets()[0]
    row=sheet.nrows
    shuju=[]
    for i in range(1,row):
        shuju.append(sheet.row_values(i))
    return shuju
