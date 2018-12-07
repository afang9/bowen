# xiaom={'name':'小明',
#        'sex':'12',
#        'grade':'tree'}
# """打印的键值对key对应的value"""
# print(xiaom['name'])
# """增加"""
# xiaom['爱好']='篮球'
# print(xiaom)
# """{'name': '小明', 'sex': '12', 'grade': 'tree', '爱好': '篮球'}"""
# xiaom['sex']=34
# print(xiaom)
# """{'name': '小明', 'sex': 34, 'grade': 'tree', '爱好': '篮球'}"""
# """删除"""
# xiaom.pop('爱好')
# print(xiaom)
# """{'name': '小明', 'sex': 34, 'grade': 'tree'}"""
# xiaom.popitem()
# """{'name': '小明', 'sex': 34}默认删除最后一个"""
# print(xiaom)
# xiaom={'name':'小明',
#        'sex':'12',
#        'grade':'tree'}
# print(len(xiaom))
# new_dict={'小刚':'男',
#           '小红':'女'}
# xiaom.update(new_dict)
# """{'name': '小明', 'sex': '12', 'grade': 'tree', '小刚': '男', '小红': '女'}"""
# print(xiaom)
# xiaom.clear()
# print(xiaom)
# xiaom['sex1']=[1,2,3,45,5]
# """{'name': '小明', 'sex': '12', 'grade': 'tree', '小刚': '男', '小红': '女', 'sex1': [1, 2, 3, 45, 5]}"""
# print(xiaom)
# print(xiaom['sex1'][2])
# """3"""
xiaom={'name':'小明',
       'sex':'12',
       'grade':'tree'}
# print(len(xiaom))
new_dict={'小刚':'男',
          '小红':'女'}
# print(xiaom.keys())
# """dict_keys(['name', 'sex', 'grade'])"""
# print(new_dict.items())
# """dict_items([('小刚', '男'), ('小红', '女')])"""
# print(xiaom.values())
# """dict_values(['小明', '12', 'tree'])"""
"""在一个循环里，i的取值是字典的key"""
for i in new_dict:
    print('%s--%s'%(i,new_dict[i]))
"""小刚--男
   小红--女"""

