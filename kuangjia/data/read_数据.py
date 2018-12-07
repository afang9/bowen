import xlrd
def duqu_shuju():
    shuju = []
    f = xlrd.open_workbook(r'e:\py\北京\北京.xlsx')
    sheet = f.nsheets
    sheet = f.sheets()[0]
    num = sheet.nrows
    # print(num)
    for i in range(1, num):
        aa = sheet.row_values(i)
        shuju.append(aa)
    return shuju

    # print(shuju)
#     print(shuju[1][1])
# duqu_shuju()
def read_runtes():
    with open('实例.txt','r') as g:
        c=g.read().split('\n')
    return c
# if __name__=='__main__':
#     print(read_runtes())
        # print(ceshi)
    # for i in ceshi:
    #     f=open(r'...\kuangjia\data\实例.txt','r')
    #     aaa=f.read()
    #     print(aaa)































# import xlrd
# def duqu_shuju1():
#     shuju1=[]
#     f=xlrd.open_workbook(r'E:\py\北京\名字.xlsx')
#     sheet=f.sheets()[0]
#     num1=sheet.nrows
#     for i in range(1,num1):
#         name_shuju=sheet.row_values(i)
#         shuju1.append(name_shuju)
#     # print(shuju1[0][0])
# # duqu_shuju1()
#     return shuju1