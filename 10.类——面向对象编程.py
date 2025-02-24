#类和对象
#类是从n个对象抽取出“像”的行为和属性从而归纳总结出的一种类别
#可以和C++的类类比，只不过python类中的函数更多叫做方法
#Python中一切皆对象，比如"hello sunhaoyu"属于字符串类

#自定义类：
#class name:
#   pass
#对象：object=name()
class animal:
    pass;
sunhaoyu=animal()
print(type(sunhaoyu))

#类的组成：属性=变量，方法=函数
#类属性：类当中方法外的变量，调用时可用对象名打点也可以用类名打点
#实例属性与实例方法：实例方法就像C++中的一个正常的函数，只不过自带了一个self参数，引用时用对象名打点
#一个特殊的实例方法：类似于构造函数,__init__，只不过python中可以在其内部直接定义实例属性
#类方法和静态方法：类似于C++中的静态函数，都是对类来说的，调用时要用类打点，且方法内部不能调用实例属性与方法
class Student:
    school='YWGZ'
    #实例方法与属性
    def __init__(self,name,grade,whichclass):
        self.name=name
        self.grade=grade
        self.whichclass=whichclass
    def introduction(self):
        print(f'学校：{self.school};姓名：{self.name};年级：{self.grade};班级：{self.whichclass};')
    #静态方法与类方法：
    @staticmethod
    def clarify():
        print('This is a staticmethod.')
    @classmethod
    def clarifytwo(cls):#cls-->class
        print('This is a classmethod')
sunhaoyu=Student('孙浩宇',20,4)
sunhaoyu.introduction()
Student.clarify()
Student.clarifytwo()

#动态绑定实例与动态实例方法：
#动态绑定是对于对象进行绑定的，同类的其他对象没有
def kobe():
    print('man,hahaha')
sunhaoyu.gender='男'
sunhaoyu.haizi=kobe#注意这里是赋值，不要小括号
sunhaoyu.haizi()#man,hahaha

#面向对象的三大特征：

#特征一：封装（访问权限）
#其实就是C++中的可见性（public，protected，private）
#另外封装可以理解为一堆元件封装成一个芯片，集中体现最后的功能
#单下划线开头：protected——允许类自身和子类使用，但实际有方法用外部代码访问（防君子不防小人）
#双下划线开头：private——只允许类本身使用
#首尾双下划线：一般表示特殊方法，比如__init__()
#其他就是public，只不过不像C++要声明
#下面这个例子主要讲怎样在外部用protected和private属性或方法
class examplespace:
    def __init__(self,variableone,variabletwo):
        self._variableone=variableone
        self.__variabletwo=variabletwo
    def __function(self):
        print(self.__variabletwo)
ex=examplespace(0,1)
print(ex._examplespace__variabletwo)
ex._examplespace__function()
#可以像上面这种形式访问的原理：先用dir()函数查看类内部所有属性和方法，呈现出的就是每一个属性和方法的调用形式
print(dir(ex))
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__'
# '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__'
# '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__'
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__'
# '__subclasshook__', '__weakref__',  '_examplespace__function', '_examplespace__variabletwo', '_variableone']
#从上面可以看出怎样调用protected属性或方法，如下
print(ex._variableone)
#事实上，上面这种访问protected/private属性或方法的方式极不推荐，既不美观又很难写
#可用@property转方法为属性使用，但是这样只能看属性的值而不能改，如果要改的话要对转换过来后的属性进行setter设置
#用例如下：
class people:
    def __init__(self,name,gender):
        self.name=name
        self.__gender=gender
    #注意函数的命名都是要进行转化的变量
    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self,variable):
        try:
            if variable!='男' and variable!='女':
                raise Exception('WTF?')
            else:
                self.__gender=variable
        except Exception as e:
            print(e)
human=people('孙浩宇','男')
print(human.gender)
human.gender='女'#调用方式就像是对属性赋值，有点像C++里面的隐函数
print(human.gender)
human.gender='xiu男娘'

#特征二：继承
#和C++不同，python中一个子类可以同时继承n个父类，相同的是一个父类可以同时拥有多个子类
#若没有说明，一个类默认继承的是object类
#子类拥有父类的public/protected属性/方法
#语法：class name(father1,father2...):
class plant:
    def __init__(self,name):
        self.name=name
    def plant_show(self):
        print('This plant is called',self.name)

class apple(plant):
    def __init__(self,name,color):
        super().__init__(name)
        #使用super().__init__(...)调用父类的__init__
        #如果有多个父类，如FatherA,FatherB则要用FatherA.__init__(...)
        self.color=color
    #方法重写：和C++一样，方法重写要求名字必须和父类一样
    #如果要在重写中调用父类的原方法，要用super().origin_function_name(..)
    #有多个父类与上同理
    def plant_show(self):
        super().plant_show()
        print('The color of this plant is',self.color)

sunhaoyu=apple('三千铁块','小男娘')
sunhaoyu.plant_show()

#特征三：多态
#Python中的多态最不一样的点在于只关心行为
#即不关心一个类到底是什么类型，有没有继承，只要都有同一个方法，即构成多态
#程序会在运行时判断数据类型进而具体到方法
class small:
    def say(self):
        return '小男娘'
class middle:
    def say(self):
        return '中男娘'
class large:
    def say(self):
        return '大男娘'
def wow(obj):
    return obj.say()
sunhaoyu=small()
haoyusun=middle()
sanqiantiekuai=large()
lst=[sunhaoyu,haoyusun,sanqiantiekuai]
for item in lst:
    print('sunhaoyu是一个'+wow(item))


#object类
#在之前用了dir()查看类里面所有的组成，可以发现其中除了自己写的内容之外，还有一些不认识的成分
#这些成分都是从父类object中继承来的，所有的类都直接或者间接继承于object
#其中有三个比较重要的特殊方法
#__init__()
#__new__()：系统用来给对象开辟空间，调用一定在init之前
#__str__()：描述类，返回值为str，如果没有重写返回的就是类的地址（一个比较奇怪的东西）
print(sunhaoyu)#<__main__.small object at 0x0000011B0C61D340>
#上面这种直接print对象的就是调用了__str__，可以重写
class per:
    def __str__(self):
        return '这是sunhaoyu小朋友的类'
sunhaoyu=per()
print(sunhaoyu)#这是sunhaoyu小朋友的类
#从这个角度来看为什么说python中一切皆对象
a=10
print(dir(a))
#['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__'
#'__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__'
#'__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__'
#'__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__',
# '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__radd__', '__rand__'
#'__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__'
#'__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__'
#'__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__'
#'__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__'
#'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes'
#'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
#可以发现很多运算符其实就是里面的特殊方法，比如+就是__add__，!=就是__ne__
#对LateX熟悉的话会好辨认很多
#除了特殊方法还有特殊属性，用上面的plant类举例：
sunhaoyu=apple('小南量','涩涩的')
print(sunhaoyu.__dict__,sunhaoyu.__class__)
print(apple.__bases__)#返回父类元组，如果用__base__，只返回第一个父类
print(apple.__base__)
print(apple.__mro__)#层次结构元组(<class '__main__.apple'>, <class '__main__.plant'>, <class 'object'>)
print(plant.__subclasses__())#子类列表，注意这一个特殊属性要带小括号

#深拷贝和浅拷贝
#赋值：对象和子对象对应的是一个东西
#浅拷贝：对象不是一个东西，但是子对象是一个东西
#深拷贝：对象和子对象都不是一个东西
#Python中的深拷贝和浅拷贝不像C++里面的复杂，导入模块即可
class CPU:
    pass
class DISK:
    pass
class computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
cpu=CPU()
disk=DISK()
com=computer(cpu,disk)
import copy
comlightcopy=copy.copy(com)
comdeepcopy=copy.deepcopy(com)
print(com,com.cpu,com.disk)
print(comlightcopy,comlightcopy.cpu,comlightcopy.disk)
print(comdeepcopy,comdeepcopy.cpu,comdeepcopy.disk)
#观察return回来的地址就能看出区别了