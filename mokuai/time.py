import time
import datetime

# print(time.time())   # 获取当前时间时间戳
# print(time.altzone)  # 返回与utc时间的时间差,以秒计算
# print(time.clock())  # 返回处理器时间
#
#
# print(time.strptime('2018/05/19','%Y/%m/%d'))#         自定义格式化字符串   --> strcut_time
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))#    strcut_time  --> 自定义格式化字符串
# print(time.mktime(time.localtime()))    #                          strcut_time --> 时间戳
# print(time.asctime())   #                                          strcut_time --> Sat May 19 23:51:04 2018
# print(time.ctime())     #                                               时间戳 --> Sat May 19 23:51:48 2018
# print(time.gmtime())    #返回utc时间的struc时间对象        加参数:      时间戳 --> strcut_time (utc)
# print(time.localtime()) # 获取本地时间的struct_time 对象   加参数：     时间戳 --> strcut_time (local)
#

# 打印返回格式(固定)
print(datetime.datetime.now())
# 返回一组数据(年,月,日,小时,分钟,秒,微秒)
print(datetime.datetime(2017,4,12,11,21,2,112122))
# 时间加(减),可以是日,秒,微秒,毫秒,分,小时,周
#days=0, seconds=0, microseconds=0,milliseconds=0, minutes=0, hours=0, weeks=0
print(datetime.datetime.now()+datetime.timedelta(days=12))
print(datetime.datetime.now()-datetime.timedelta(days=12))
#时间替换
print(datetime.datetime.now().replace(day=1,hour=10))
# 2018-05-01 10:20:28.957783