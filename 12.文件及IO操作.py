#文本文件和二进制文件：没什么可说的

#文件的基本操作步骤：打开-操作-关闭
#打开文件name=open(filename,mode,encoding)
#使用写的模式打开时，如果文件不存在那么则会自动新建一个这样的文件；使用读的文件打开会报错
#mode和C语言中的'w','r'等一样
'''
def my_file():
    fp=open('test.txt','w',encoding='utf-8')
    fp.write('什么罐头我说')
    result=fp.read('test.txt','r',encoding='utf-8')
    fp.close()
    这样写是报错的
'''
def my_file():
    fp=open('test.txt','w',encoding='utf-8')
    fp.write('什么罐头我说')
    fp.close()
    fp=open('test.txt','r',encoding='utf-8')
    result=fp.read()
    print(type(result),'  ',result)#<class 'str'>    什么罐头我说
my_file()#第一次写的时候没有txt文件，现在可以发现出现了test.txt
#一些文件的基本操作：
#read(size):不解释，返回结果为str，size是指定的字符数
#readline(size):读一行，如果制定了size，则读取这一行中size大小的数据
#readlines(size):读取文件中所有的数据，结果为列表
#write(string):写入字符串
#writelines(lst):将内容全部为string的列表写入文件
#seek():和C语言相似，改变当前指针的位置（英文字符一字节，中文gbk编码两字节，utf-8编码三字节）
def my_file_read(file,size):
    fp=open(file,'r',encoding='utf-8')
    result_lines=fp.readlines(size)
    fp.close()
    print(result_lines)
def my_write_lst(file,lst):
    fp=open(file,'a',encoding='utf-8')
    fp.writelines(lst)
    fp.close()

lst=[['\n三千铁块\n','hahaha\n'],['man\n'],['what can i say\n'],['123\n']]
for item in lst:
    my_write_lst('test.txt',item)
my_file_read('test.txt',10)#['什么罐头我说\n', '三千铁块\n']
#一行是一个str元素
#关于seek
def seek_function(filename,string_content,position):
    file=open(filename,'w+',encoding='utf-8')
    file.write(string_content)#这个时候指针在最后，直接读什么都读不到，要全部读就要用seek把指针放到开头
    file.seek(position)
    print(file.read())
    file.close()
seek_function('test_another.txt','haha',2)#ha
#通过上述操作可以实现文件复制
def image_copy(src,new_path):
    src_image=open(src,'rb')#二进制文件打开不需要encoding
    new_image=open(new_path,'wb')
    middle=src_image.read()
    new_image.write(middle)
    src_image.close()
    new_image.close()
    print('Copy successfully')
image_copy('image.png','image_copy.png')
#还可以写成./image.png和./image_copy.png，./代表当前目录，如果要写其他目录，要写../filegroup_name/file_path

#with语句
#with语句又称上下文管理器，其作用是打开文件后无论是否发生异常（或者源码中忘了关文件），最终都能保证文件关闭，这个过程是自动的
#with open() as file:pass
#可以用with语句对上面的函数进行改写
def image_copy(src,new_path):
    with open(src,'rb') as src_image:
        middle=src_image.read()
        with open(new_path,'wb') as copy_image:
            copy_image.write(middle)
            print('Copy successfully(\'with\')')
image_copy('./image.png','./image_copy.png')


#Py中的数据维度

#一维数据：（线性存储）。列表（用的最多）、元组、集合and so on
def dimone_write(data_dimone,file_path):
    #写入csv（分割值文件，纯文本文件表示表格数据）文件，用write加join实现
    data_dimone_string=','.join(data_dimone)
    with open(file_path,'w') as dimone_file:
        dimone_file.write(data_dimone_string)
def dimone_read(file_path):
    with open(file_path,'r') as dimone_file:
        result=dimone_file.read().split(',')
        print(result)

data_dimone=['x','y','z','alpha']
dimone_write(data_dimone,'Dimone_Data.csv')
dimone_read('Dimone_Data.csv')#['x', 'y', 'z', 'alpha']

#二维数据：以列表为元素的列表，用行列来刻画（有点像C中的二维数组），最典型的应用就是numpy数组
def dimtwo_write(data_dimtwo,file_path):
    with open(file_path,'w') as dimtwo_file:
        for item in data_dimtwo:
            str_item = ','.join(item)
            dimtwo_file.write(str_item)
            dimtwo_file.write('\n')

def dimtwo_read(file_path):
    with open(file_path, 'r') as dimtwo_file:
        read_lines=dimtwo_file.readlines()
        for item in read_lines:
            result=item[:len(item)-1].split(',')
            print(result)
    #实现办法：二维转一维

data_dimtwo=[['x','y','z'],['1','1','1'],['2','2','2']]#注意这里的1，2要是字符串，这个特别在numpy中很重要
dimtwo_write(data_dimtwo,'Dimtwo_Data.csv')
dimtwo_read('Dimtwo_Data.csv')
'''
['x', 'y', 'z']
['1', '1', '1']
['2', '2', '2']
'''

#高维数据：用的是Key-Value模式（字典）存储
#Py中的json模块专门处理JSON（JavaScript Object Notation）格式储存的数据，不像一维数据和二维数据要手动转为str
#json.dumps(obj)：编码——转pyhton数据类型为JSON格式
#json.loads(obj)：解码——转JSON格式为python数据
#json.dump(obj,file)：从文件中读取执行dumps
#json.load(file)：转换后写入file
lst=[
    {'name':'小男娘','age':18},
    {'name':'中男娘','age':18},
    {'name':'大男娘','age':18}
]
import json
lst_json=json.dumps(lst,ensure_ascii=False,indent=4)#第二个参数是不让中文乱码，第三个是缩进
print(type(lst_json),lst_json)#<class 'str'>
lst_back=json.loads(lst_json)
print(type(lst_back),lst_back)
with open('Json.txt','w') as json_write:
    json.dump(lst,json_write,ensure_ascii=False,indent=4)#进去之后乱码是编码格式的问题，reload为gbk就可以了
with open('Json.txt','r') as json_read:
    lst_back=json.load(json_read)
    print(lst_back)


#os模块的一些常用方法
#ps：目录约等于文件夹
import os
print(f'当前工作路径：{os.getcwd()}')
print(f'当前路径下所有目录及文件：{os.listdir()}')
print(f'指定路径下所有目录及文件：{os.listdir('E:\code\python_pycharm\pylearning_basedC\.venv')}')
#在当前路径下创建目录，不能创建已经存在的目录
#os.mkdir('三千铁块')
#连续创建
#os.makedirs('./sunhaoyu/nanniang/xiaonanniang')
#删除当前路径下空目录，如果要删除的文件不存在会报错
#os.rmdir('./三千铁块')
#删除多级目录
#os.removedirs('./sunhaoyu/nanniang/xiaonanniang')
#改变工作路径
os.chdir('./test_chap')
print(f'改变后的工作路径：{os.getcwd()}')
#通过递归方法遍历目录树（指定路径下所有的目录and目录里面的目录/文件and......）
for dir,dirlist,filelist in os.walk('E:\code\python_pycharm\pylearning_basedC'):
    print(dir)
    print(dirlist)
    print(filelist)
    print('________________________________')
#删除指定文件:os.remove(path)
#给指定文件重命名：os.rename(old,new)
#获取文件信息
os.chdir('E:\code\python_pycharm\pylearning_basedC')
import time
def time_format(time_struct):
    result=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time_struct))
    return result
file_info=os.stat('./test.txt')
print(type(file_info))#<class 'os.stat_result'>
print(file_info)
print(type(time_format(file_info.st_atime)))
print('最近一次访问的时间：',time_format(file_info.st_atime))
print('文件创建时间（Windows11）：',time_format(file_info.st_ctime))
print('最近一次修改的时间：',time_format(file_info.st_mtime))
print('文件大小',file_info.st_size,'bytes')
#启动电脑中随便哪个文件，比如计算器
#os.startfile('calc.exe')
#os.startfile('C:\Program Files\Tencent\WeChat\WeChat.exe')

#os中子模块path的一些常用方法
from os import path as pt
print('获取绝对路径:',pt.abspath('./test.txt'))
print('判断文件/目录在磁盘上是否存在:',pt.exists('test.txt'))#相对路径
print('判断文件/目录在磁盘上是否存在:',pt.exists('./etest.txt'))
print('拼接路径：',pt.join('E:\code\python_pycharm\pylearning_basedC','test.txt'))
print('分割文件名与后缀名：',pt.splitext('test.txt'))
print('提取文件名：',pt.basename(r'E:\code\python_pycharm\pylearning_basedC\test.txt'))#注意用r
print('提取路径：',pt.dirname(r'E:\code\python_pycharm\pylearning_basedC\test.txt'))#注意用r
print('判断给定目录是否有效',pt.isdir('E:\code\python_pycharm\pylearning_basedC'),
      pt.isdir('E:\code\python_pycharm\pylearning_basedD'))
      #注意是判断目录的，放文件的路径会判定为False