#关键字和标识符和C中的规则一样
#py的标识符可以用中文但是不建议，标识符可以有数字但不能放在开头
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
#关键字是严格区分大小写的
#标识符规范：常量采用全大写，多单词用_分隔，类采用Pascal风格，单词首字母大写，如MyClass
pi=3.1415926#变量
PI=3.1415926#常量
#命名谨慎使用i和O（大写的O），采用有意义的单词，不要命名a，b，c...
#类中类可以用_开头，如_innerMyClass,注意python中_开头不能乱用，使用双下划线开头可以类比C++的类里面的m_
#双下划线开头/结尾是python特有的，比如__init__()表示初始化函数
#以上在面向对象的编程中（可以类比C++）才会用到

#py的变量
luck_number=8
print("luck_number的类型：",type(luck_number))
luck_number="孙浩宇"
print("luck_number的类型：",type(luck_number))
#python的变量是动态变量，可以通过直接赋予不同的值来修改一个变量的类型
no=number=1234
print(id(no),id(number))
#python中允许连赋值,并且和C类语言不同，C类语言两个变量值相同，他们的地址不同
#在python中，两个变量值相同，他们的地址相同
#也就是说，python中虽然没有指针的概念，但是可以把变量理解为C中的指针
#标识符在栈内存中，指向了堆内存中的数值

#数据类型
#数值型
#int型：十进制，二进制（0b\0B），八进制（0o\0O），十六进制（0x\X），print时默认以十进制输出
number=1234
number1=0b1010
number2=0o1377
number3=0x198AF
print(number,number1,number2,number3,sep=" ")
#浮点型：python中的浮点数与C类语言不同，没有float与double之分，但是运算时同样都具有精确度带来的不确定性
print(0.1+0.2)
print(round(0.1+0.2,2))#round(value,digits)
#py的科学计数法：E
float_number=1.99E-45
print(float_number)
#py中是可以表示虚数的，其规则与数学上的复数完全一致，j=i，实数部分用.real，虚数部分用.imag
float_number=123+567j
print(float_number.real,float_number.imag,sep=" ")
#字符串型
#字符串界定符：单引号，双引号，三引号（三对单引号或三对双引号）
#三引号之所以可以用为注释，使因为python在只有字符串的时候不会执行，当本质上还是字符串
#由此也可知，三引号可以用来写多行字符串
lover='''孙浩宇啊啊啊
刚满十八岁
好棒哦'''
print(lover)
#转义字符和C类语言应用一样，原字符是使转义字符失效的字符，r\R
print("\"小黑好想要\"")
print(R"\"小黑好想要\"")
#字符串的索引和切片
#可以从C语言的数组角度出发就十分好理解，无非反向的时候最后一位从-1开始
print(lover[5])#可见lover[5]='\n'
print("hello"[4],"hello"[-1],sep=" ")
print(lover[:3],lover[-3:],lover[5:-1],lover[3:1],lover[-3:2],lover[-3:-8],sep="#")
#注意默认情况的起始\结尾为0,[]不包含右端点
#可以发现lover[3：1],lover[-3:2],lover[-3:-8]什么都没有,也就是说字符串不能完成到头后重新开始的输出\反向输出
#三个字符串常用操作
#链接：x+y，之前有了
#复制：n*x或者x*n
example1="2024."
example2="1.13"
print(5*example1)
#查找，输出结果是“True”或者“False”
print("2023"in example1,"2024"in example1,sep="   ")
#bool型：只有0=False，1=True，bool函数可测试变量的布尔值
print(bool(-5))#非零为真
print(bool("京"),bool(""),bool(None),sep=" ")#非空为真
#python中一切皆对象，任何对象都有一个bool值，这与C类语言是不同的

#数据类型转换
#隐式类型转换：直接赋值来转换
#显式：type(varible)
#int,float,str,chr,ord（chr的逆，字符变整型）,hex、orc、bin（整型->十六进制、八进制、二进制字符串）
x=10
y=3
z=x/y
print(round(z,2),type(z))#隐式
print(float(x),hex(x),sep=" ")#显式
print(hex(1234),type(hex(1234)))#<class 'str'>
#字符串显式转换中会报错的情况：
#转为int：转不是十进制的字符串（这和C语言不一样），字符串是小数形式
#转为float：字符串含非十进制数字

#eval函数：
#input输入的都是字符串，eval的作用就是去掉字符串的引号，是类型转化函数
#常与input搭配使用
sums=eval(input("输入："))
print(round(sums,2),type(sums))
#注意：eval实际是去除字符串变量的引号，返回去除后的变量
#如果直接写print(eval("hello"))，eval返回的是hello这个变量，如果之前没有定义过一个hello变量则会报错
#正确操作：
sentence="hello"
print(eval("sentence"))#注意引号，没有引号就相当于要输出hello变量，但是没有变量叫hello
sentence="1+1.2"
formation=eval(sentence)#这里又没有引号，如果有引号下面输出的就是个字符串1+1.2
print(formation)
#总结：eval里面有引号去引号，没有引号去变量里面的引号，去除操作只做一次
#如果里面不是算式且满足变量命名要求，那么返回的是一个变量不是变量的值