#模块：
#模块就是py文件，标准的模块命名只能由小写字母、不同单词用下划线连接来组成
#模块就是将具有相同功能的代码写在一起，减少代码重复率和提升效率
#所以之前所有的py文件都是不规范的
#模块具有系统模块——即开发人员写的模块；和自定义模块
#下面所有代码用的自定义模块为pylearning_basedC下的my_info.py

#模块的导入：两种导入方式
#1.from ... import ...：只导入模块的部分，其中*号是通配符
from my_info import name
print(name)
from my_info import *
intrduction()
#2.import ... [as another_name]：全部导入，且可以起别名
#这种方式可以导入多个模块，模块之间用逗号隔开，如果这些模块中有相同的变量/函数，前者会被后者覆盖
#想要用前者中同名的变量/方法只能用‘模块名.变量/函数’来用，虽然一般来说都是没有同名的也习惯这么用
import my_info as mine
mine.intrduction()

#Python的包：
#包是含有__init__.py文件的一个文件夹，命名规则和模块一样
#包的作用是可以将功能类似的模块放在一起，同时避免因模块名相同而产生的冲突
#下面所有代码用的自定义包为pylearning_basedC下的admin
#可以发现新建“Python软件包”后自动生成了__init__.py文件，可以在里面写东西
#导入规则和模块一模一样
import admin.my_admin as mine
mine.intrduction()#可以发现，只导入了admin.my_admin，却输出了__init__中的版权——Minijie3 \n HITsz
from admin.my_admin import name
print(name)#之后__init__不会再输出了
from admin import my_admin
mine.intrduction()#可以发现__init__的内容只输出了一次

#主程序运行：if name=='main'
#作用在于将导入的模块中不需要/不能被执行的代码变为非全局化，这样被主程序包装的代码就不能被执行了
#比如说如果前面写的所有从1到10的代码命名规范可以作为模块导入，那么其中所有的代码都是执行的，因为都没在主程序里面写
#例子：如pylearning_basedC下的modelA.py导入dodelB.py


#Python中常用的内置模块
#内置模块是在安装Python解释器时一起安装的，一般有200多个

#下面仅仅浅浅说几个简单的，其他的想学网上资源多的是
#re：正则表达式相关

#random：产生随机数模块
#python产生随机数的规则和C语言一样，都是通过种子来实现的，也就是如果你种子设的一样，产生的随机数就是一样的
#只不过在python中不需要你手动设，因为你不设解释器会默认种子为当前时间
import random
random.seed(10)
print(random.random())#你运行多少次都是0.5714025946899135，因为seed被定了
#random()产生0到1之间的数字，左闭右开
#randint()是[1,100]的整数
#randrange(a,b,k):[a,b),step=k
#uniform(a,b):[a,b]小数
#choice(lst)：从lst中随机选择一个元素返回
#shuffle(lst)：将lst按某顺序打乱，由于是对列表本身操作，所以无返回值
print(random.randint)
for i in range(1,10):
    print(random.randrange(1,20,3),end=',')
print()
print(random.uniform(1,100))
lst=['蔡徐坤','范丞丞','陈立农']
print(random.choice(lst))
print(random.shuffle(lst))#None
print(lst)

#time：python中用于处理时间和格式化时间等功能的模块
#time():获取当前时间戳
#localtime(sec)：根据给的时间戳返回一个struct_time
#ctime()：根据当前时间戳返回对应的易读字符串
#strftime(format，time)：str——字符串，f——格式化，对struct_time进行格式化转为字符串，format自己定
#strptime(string,format):上面这个的逆，但是注意参数位置
#sleep(sec)：程序休眠sec秒
#时间的格式化：%Y年,%m月份,%B月名,%d日,%A星期,%H小时24h制,%I小时12h制,%M分钟,%S秒,只有月份和日期小写
import time
print(time.time())#1710922939.7170868
print(time.localtime(60))
#time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=8, tm_min=1, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
#由于localtime返回的是本地时间，北京时间属于东八区，所以根据时间戳计算的结果是从1970年1月1日8：00 a.m.星期四开始的
#注意tm_wday=0对应的是星期一
print(time.localtime(time.time()))
print(time.ctime())#Wed Mar 20 16:24:35 2024
print(time.strftime("%Y-%B-%d",time.localtime()))
time.sleep(1)
print(time.strptime('2024-03-20',"%Y-%m-%d"))