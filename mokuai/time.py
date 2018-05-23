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
# 格式字符及意义
# %a 星期的简写。如 星期三为Web
# %A 星期的全写。如 星期三为Wednesday
# %b 月份的简写。如4月份为Apr
# %B月份的全写。如4月份为April
# %c:  日期时间的字符串表示。（如： 04/07/10 10:43:39）
# %d:  日在这个月中的天数（是这个月的第几天）
# %f:  微秒（范围[0,999999]）
# %H:  小时（24小时制，[0, 23]）
# %I:  小时（12小时制，[0, 11]）
# %j:  日在年中的天数 [001,366]（是当年的第几天）
# %m:  月份（[01,12]）
# %M:  分钟（[00,59]）
# %p:  AM或者PM
# %S:  秒（范围为[00,61]，为什么不是[00, 59]，参考python手册~_~）
# %U:  周在当年的周数当年的第几周），星期天作为周的第一天
# %w:  今天在这周的天数，范围为[0, 6]，6表示星期天
# %W:  周在当年的周数（是当年的第几周），星期一作为周的第一天
# %x:  日期字符串（如：04/07/10）
# %X:  时间字符串（如：10:43:39）
# %y:  2个数字表示的年份
# %Y:  4个数字表示的年份
# %z:  与utc时间的间隔 （如果是本地时间，返回空字符串）
# %Z:  时区名称（如果是本地时间，返回空字符串）