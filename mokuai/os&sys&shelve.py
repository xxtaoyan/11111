import os

print(os.pathsep)  # 输出用于分割文件路径的字符串
print(os.pardir)  # 获取当前目录的父目录字符串名：('..') 'parent 父亲，根源 ，起源'
print(os.linesep)  # 输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
print(os.sep)  # 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
print(os.name)  # 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'

path1 = os.getcwd()
path = os.path.join(path1, 'text.txt')

f = open(path, 'w')  # 当前目录创建 text.txt
f.close()
print(os.stat(path))  # 获取文件/目录信息 返回一个元组
print(os.listdir(path1))  # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.rename('text.txt', 'rename.txt')  # 重命名文件/目录

print(os.path.split(path))  # 将path分割成目录和文件名二元组返回 'split 分裂，分开'
print(os.path.dirname(path))  # 返回path的目录。其实就是os.path.split(path)的第一个元素
print(os.path.basename(path))  # 返回path最后的文件名。path以／或\结尾，返回空值。os.path.split(path)的第二个元素
print(os.path.abspath(path))  # 返回path规范化的绝对路径
print(os.path.join(path1, 'text.txt'))  # 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
print(os.path.getatime(path1))  # 返回path所指向的文件或者目录的最后存取时间 'get access time'
print(os.path.getmtime(path1))  # 返回path所指向的文件或者目录的最后时间 'get modify(修改) time'
print(os.path.getctime(path1))  # 返回path所指向的文件或者目录的创建改时间 'get create time'
print(os.path.getsize(path1))  # 返回path所指向的文件或者目录的大小

print(os.path.exists(path1))  # 如果path存在，返回True；不存在，返回False ‘exists 存在‘
print(os.path.isabs(path))  # 如果path是绝对路径，返回True
print(os.path.isfile(path))  # 如果path是一个存在的文件，返回True。否则返回False
print(os.path.isdir(path1))  # 如果path是一个存在的目录，则返回True。否则返回False


print(os.curdir)  # 返回当前目录相对路径: ('.')  ‘current directory’
print(os.getcwd())  # 获取， 当前python脚本工作目录路径  'current working directory'
print(os.environ)  # 获取系统环境变量 ’environ 环境‘

os.remove('rename.txt')  # 删除一个文件

os.mkdir('text')  # 生成单级目录，已存在，报错 相当于shell中的 mkdir dirname
os.rmdir('text')  # 删除单级目录，若目录不为空，则无法删除，相当于shell中的rmdir dirname
os.makedirs('text/text')  # 生成多层递归目录 已存在 报错
os.removedirs('text/text')  # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除
#
# os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd
os.system("ipconfig")  # 运行shell命令，直接显示

import sys


print(sys.argv)  # 命令行参数List，第一个元素是程序本身路径
# sys.exit(0)  # 退出程序，正常退出时exit(0)
print(sys.version)  # 获取Python解释程序的版本信息
print(sys.maxunicode )   # 最大的Int值
print(sys.path)   # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print(sys.platform)  # 返回操作系统平台名称
sys.stdout.write('please:')
val = sys.stdin.readline()[: -1]
