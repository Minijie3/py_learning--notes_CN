#自定义函数结构：
#def 函数名 (参数列出(形参，调用时传入的实参))
#函数体
#（如有返回值）return 返回值行出
def get_sum(start,end):
    try:
        if start<end:
            sum = 0
            for i in range(start,end+1):
                sum+=i
            return sum
        else:
            raise Exception('规定start应小于end')
    except Exception as e:
        print(e)

print(f'1到100之和（包含端点）为{get_sum(1,100)}')
print(f'100到1之和（包含端点）为{get_sum(100,1)}')

#关于参数：
#实参个数必须等于形参个数并且必须一一对应
#这里可以发现，python中函数调用时会给出提示，这一点和C不一样，这避免了传入参数类型不匹配而引起的报错
#还可以用另一种方式实现这样的功能，即关键字传参，但要求关键字必须与形参名称相同,如下面的实例
def happy_birthday(name,age):
    print(f'祝{name}{age}岁生日快乐')

happy_birthday(name='xxx',age=18)
happy_birthday('xxx',age=18)
#但是注意happy_birthday(name='xxx',18)语法错误(SyntaxError)
#因为违反了原则：位置参数必须在关键字参数之前
#默认值传参：直接对形参赋值，如果有一个参数没有赋值，则采用默认值，否则采用传入的值，默认值在函数定义处完成
def happy_birthday(name='xxx',age=18):
    print('祝'+name+str(age)+'岁生日快乐')

happy_birthday()
happy_birthday('yyy')
happy_birthday(age=20)
#注意happy_birthday(20)报错，20被赋给了name，这说明位置参数和默认值参数同时存在时，默认值参数必须在后
#可见和默认值参数搭配，最好用的解决方法就是用关键字传参
#可变参数：
#可变位置参数：参数前面带*，可以传入任意数量的位置参数，最终组成一个tuple进入形参中
#可变关键字参数：参数前面带**，可以传入任意数量的关键字参数，最终组成一个dict进入形参中
def pos_function(*para):
    print(type(para))
    for item in para:
        print(item,end=' ')
    print()
pos_function(1,2,3,4)
pos_function([1,2,3,4])
pos_function(*[1,2,3,4])#利用*对传入的列表做解包
def key_function(**kwpara):
    print(type(kwpara))
    for key,value in kwpara.items():
        print(f'{key}----{value}',end=',')
    print()
key_function(apple=12,student=25)
dictionary=dict(apple=12,student=25)

#关于返回值：
#python的返回值同样通过return返回，但区别在于函数可以返回多个值，返回多个值的时候以元组的形式返回
#下面是利用python返回值的特点写的二元函数f(x,y)=xy/(x+y)
def caculate(numone,numtwo):
    return numone+numtwo,numone-numtwo
def mutiple(numone,numtwo):
    return numone*numtwo
def sums(numone,numtwo):
    return numone+numtwo
def f_x_y(point):
    return (mutiple(point[0],point[1]))/(sums(point[0],point[1]))
print(f_x_y(caculate(4,5)))

#关于python的变量作用域
#基本和C一样，唯一的不同在于可以在函数里面定义全局变量，用到的是globle关键字
a_num=100
def variabletest(numone,numtwo):
    global variable
    variable=150
    a_num=200#和C一样，局部覆盖全局，但不影响全局
    #注意，global定义全局变量赋值必须分开写，不能写成global variable=150
    return a_num+variable+numone+numtwo
print(variabletest(1,2))
print(variable)

#匿名函数lambda：
#指的是没有名字的函数，在函数体只有一句话或者返回值只有一个时用于简化
#function=lambda 参数:表达式
#用lambda来表达之前写的f(x,y)更直观
f_xy=lambda x,y:x*y/(x+y)#<class 'function'>
print(type(f_xy),round(f_xy(1,2),4))
student_grade=[{'姓名':'孙浩宇','成绩':59},
     {'姓名':'马+7','成绩':58},
     {'姓名':'丁x心','成绩':57},
     {'姓名':'宋亚轩','成绩':56}]
student_grade.sort(key=lambda x:x.get('成绩'),reverse=True)
print(student_grade)

#递归:道理都是一个，只是不同语言的表达问题
#如阶乘
def factorial(interger):
    if interger>=1:
        return interger*factorial(interger-1)
    else:
        return 1
print(factorial(4))
#再比如Fibonacci数列：a_n=a_(n-1)+a_(n-2)
def Fibonacci_array(index):
    if index>=3:
        return Fibonacci_array(index-1)+Fibonacci_array(index-2)
    elif index==1 or index==2:
        return 1
print(Fibonacci_array(2),Fibonacci_array(5),Fibonacci_array(9))

#python中常见的内置函数
#常用的数据类型转换函数（easy，略）
#常用的数学函数：abs()求绝对值,divmod(a,b)求a对b的商和余数,max(sequence),min(sequence)（可迭代对象）
#sum(iter)对可迭代对象进行求和,pow()幂,round()小数点，如果只有一个参数，保留整数
print(round(3.14159265358))
#常用的迭代器操作函数：对象是可迭代对象
#sorted(),reversed()反向（返回迭代器对象）,zip(),enumerate(),next(),all()检查可迭代对象里面是不是都是True
#any()检查可迭代对象里面是不是都是False(注意全部是False返回的是False)
#next(),filter(function,iter)通过指定条件过滤iter，map(function,iter)通过指定function对iter进行操作
lst=[12,101,89]
asc_lst=sorted(lst,reverse=False)
nasc_lst=reversed(lst)
print(f'升序排列：{asc_lst},倒序排列：{list(nasc_lst)}')
lst2=['马+7','丁x心','三千铁块']
creat_object=zip(lst2,lst)
print(type(creat_object))#<class 'zip'>
for i in range(1,3):
    print(next(creat_object),end=',')
print()
print(dict(creat_object))#只剩下{'三千铁块': 89}
for index,item in enumerate(lst2,start=100):
    print(f'{index}:{item}',end='    ')
print()
def judgeone(anum):
    return anum%2==0
ulst=[judgeone(lst[item]) for item in range(0,len(lst))]
print(ulst)
print(all(ulst),any(ulst))
even_lst=filter(judgeone,range(1,10))#注意这里不需要传参
print(even_lst)#<filter object at 0x000001E254E99FF0>
print(list(even_lst))#[2, 4, 6, 8]
add_lst=map(lambda x:x+1,range(1,10))
print(list(add_lst))
fruit_lst=['Apple','Banana','Orange']
new_fruit_lst=list(map(str.upper,fruit_lst))
print(new_fruit_lst)#['APPLE', 'BANANA', 'ORANGE']
#其它内置函数如id(),type(),len(),eval()等已经提过
#format(value,format_spec)在字符串的格式化里面有实例，此外它还可以直接应用
print(format('马+7','❤^11'),format(2023.5698,'.2f'))