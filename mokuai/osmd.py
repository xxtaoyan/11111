import os


print(os.pathsep)  # 输出用于分割文件路径的字符串
print(os.pardir)  # 获取当前目录的父目录字符串名：('..')
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

print(os.path.split(path))  # 将path分割成目录和文件名二元组返回
print(os.path.dirname(path))  # 返回path的目录。其实就是os.path.split(path)的第一个元素
print(os.path.basename(path))  # 返回path最后的文件名。path以／或\结尾，返回空值。os.path.split(path)的第二个元素
print(os.path.abspath(path))  # 返回path规范化的绝对路径
print(os.path.join(path1, 'text.txt'))  # 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
print(os.path.getatime(path1))  # 返回path所指向的文件或者目录的最后存取时间
print(os.path.getmtime(path1))  # 返回path所指向的文件或者目录的最后修改时间
print(os.path.getctime(path1))  # 返回path所指向的文件或者目录的创建改时间
print(os.path.getsize(path1))  # 返回path所指向的文件或者目录的大小

print(os.path.exists(path1))  # 如果path存在，返回True；不存在，返回False
print(os.path.isabs(path))  # 如果path是绝对路径，返回True
print(os.path.isfile(path))  # 如果path是一个存在的文件，返回True。否则返回False
print(os.path.isdir(path1))  # 如果path是一个存在的目录，则返回True。否则返回False


print(os.curdir)  # 返回当前目录相对路径: ('.')
print(os.getcwd())  # 获取当前工作目录， 当前python脚本工作目录路径
print(os.environ)  # 获取系统环境变量

os.remove('rename.txt')  # 删除一个文件


#
# os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd
# os.makedirs('dirname1/dirname2')    可生成多层递归目录
# os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
# os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
# os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
# os.system("bash command")  运行shell命令，直接显示
