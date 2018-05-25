import json  # 序列化为str

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
json1 = json.dumps(data)  # json1序列化为 str 类型
print(json1)
loads = json.loads(json1)
print(loads)


import pickle  # 只能用于python 版本不同可能不兼容 序列化为 bytes

pic = pickle.dumps(data)  # pic类型
print(pic)
pick = pickle.loads(pic)
print(pick)


import shelve

db = shelve.open('shelveDict')  # 打开文件
wangzhe = db['wangzhe']     # 从文件中读取之前存储的对象
wangzhe['name'] = 'wang zhe'   # 直接对对象进行修改
db['wangzhe'] = wangzhe     # 重新存储至字典文件对象中
print(db['wangzhe'])     # 结果如下{'age': 24, 'name': 'wang zhe'}
db.close()   # 关闭文件