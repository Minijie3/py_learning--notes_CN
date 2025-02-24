#准备知识：序列和索引
#序列≈数组
#索引0；正索引=数列下标，负序列=-N到-1，N代表序列长度,用内置函数len计算
strings="helloworld"
for i in range(-len(strings),0):
    print(ord(strings[i]),end=" ")
print()
#序列切片：name[start:end:step(步长)]
print(strings[0:5:1],strings[0:5:2],sep=" ")
#一些细节可见第2节中的字符串切片，比如：
#可以发现lover[3：1],lover[-3:2],lover[-3:-8]什么都没有,也就是说
#正步长字符串不能完成到头后重新开始的输出\反向输出"
#省略[::]情况默认为：开头，结尾，步长为1
#步长为负数：实现所谓的反向输出
print(strings[-1:-len(strings)-1:-1])
print(strings[-2:-len(strings)+2:-2])
#序列的一些基本操作
print('x' in strings,'h' in strings,sep=" ")
print(max(strings),min(strings),sep=" ")
print(strings.index('l'))#print(strings.index('v'))会报错，因为压根没有v
print(strings.count('l'))
print(strings+"heihei")
print(strings*2)

#——————————————————————————————————
#组合数据类型
#注意：可变数据类型的所有在自身上操作的函数都没有返回值，用来print输出的都是None

#1.列表——序列的一种,属于可变数据类型：序列的基本操作都能用在列表上
#name=[element,...]/name=list()  del name  元素类型可以不一致，这和数组的差别很大
welcome=[1,2,'hello',4.5]
print(welcome[2]*welcome[1])
lst=list(range(1,11,2))
#lst=list(input("输入列表："))#输入的每一个字符会被作为一个元素
#print(lst)
lst2=list("hello")#list()要求参数要是个可迭代对象
print(lst,lst2)
print(lst+lst2,lst*3)
del lst
del lst2#再去输出就会报错
#列表的遍历操作：
lst=["hello",1,2,4.5]
#for循环遍历：
for item in lst:
    print(item,end="  ")
print()
for i in range(0,len(lst)):
    print(lst[i],end="  ")
print()
#enumrate:for index,item in enumrate(list),注意index是序号而不是索引
for index,item in enumerate(lst,start=1):
    print(index,":",item,sep="",end="  ")
print()
#列表的可变数据类型操作（特有操作）
print(id(lst))
lst.append("nihao")#在最后加一个元素，注意是一个元素
print(lst,id(lst))#print(lst.append())输出的是None
#元素个数可变，但是内存地址不变
lst.insert(1,"#")#在index=1的位置上插入
print(lst)
lst.remove(2)#直接删除某元素,注意括号里面的是元素不是索引
print(lst,id(lst))
#pop与remove的不同在于，pop先取出元素，再删掉
print(lst.pop(1))#pop的参数是索引不是元素
print(lst,id(lst))
print(lst[-1:-len(strings)-1:-1])
lst.reverse()#原列表上进行，所以地址仍然不变
print(lst,id(lst))
new_list=lst.copy()#拷贝列表创建一个新列表
print(new_list,id(new_list))
lst.clear()
print(lst,id(lst))
#和del不同的在于clear保存了lst
lst2=[12,89,75,45,69]
#list.sort(key=None,reverse=False),默认规则key为None，reverse为升序
#注意：规则key是按照每一个元素来说的
lst2.sort()#id不变
print(lst2)
lst2.sort(reverse=True)
print(lst2)
#字符串也可以排，规则和C一样
lst2=['banana','apple','DD']
lst2.sort(key=str.lower,reverse=True)#忽略大小写(全部转为小写)排序
print(lst2)
lst2=[12,89,75,45,69]
#另一种排序函数：sorted(list,key,reverse),创建新列表储存，原列表不变
asc_lst=sorted(lst2)
print(asc_lst)
del asc_lst,new_list
#列表生成式：list=[expressions for item in range if condition]
lst=[item*3 for item in range(1,11) if item%2==0]
print(lst)
import random
lst=[random.randint(1,11) for _ in range(1,11)]
print(lst)
#二维列表：列表嵌列表，表格数据
#遍历方法：list={[],[],[]...}/双层for
#for row in list:
#   for item in row:
#       ...
#   print()
lst=[[j*row for j in range(0,5)] for row in range(0,4)]#得到四行五列list
for row in lst:
    for item in row:
        print(item,end=" ")
    print()
del lst,lst2

#2.元组:一种不可变序列，没有增删改的一系列操作，访问和处理速度快于列表
#创造元组：name=(..,..)注意元组中就算只有一个元素，逗号也不能省略，如(10),(10,)是不一样的
#name=tuple(序列)，注意括号里面是一个序列
#元素甚至可以是列表
tpl=(1,"hello",[2,"cherno"])
print(tpl)
tpl=tuple([1,2,"cherno"])#括号里面只能是一个迭代对象
print(tpl,type(tpl))
tpl=tuple("cherno")
print(tpl,type(tpl))
#元组∈序列，序列的一些基本操作同样可适用于元组
print(10 in tpl)
#访问、遍历和列表一模一样
#元组生成式：
#元组生成式生成的不是元组，是一个生成器对象，需要转化为列表或元组才有元素，需要注意的是
#__next__函数作用的是生成器对象，相当于从生成器对象中逐个取出元素
#如果全部next了，再去转化为元组，元组中就没有元素了
#并且__next__函数不能在转化后再用，原因也是因为它的作用对象是生成器对象
tpl=(item*2 for item in range(1,4))
print(tpl)#<generator object <genexpr> at 0x0000014D068AE9B0>
print(tpl.__next__(),tpl.__next__())
tpl=tuple(tpl)
print(tpl)
tpl2=(item*2 for item in range(1,4))
tpl2=tuple(tpl2)
print(tpl2)
del tpl,tpl2

#字典：可变数据序列，和列表不一样在于字典的元素是无序的，第一个输进去的不一定就排在第一个
#key（键）必须是不可变数据类型的序列（包括元组）且不可重复
#几个键可以对应一个value（值）
#创建：1.{key:value1,..,..,}
#2.dict函数：zip映射函数，zip(lst1,lst2),key->lst1[i],value->lst2[i]
#但是zip的结果是一个zip生成对象，要转换为list，转换之后每个元素是一个(key,value)的元组
#要转为字典，就要用dict()转换
#赋值函数:dict(key1=value1,..)
print({(1,2,3):10})
dictionary={1:'dog',2:'cat',3:'apple'}
lst=[1,2,3]
lst2=['dog','cat','apple','zoo']
dictionary=zip(lst,lst2)#zoo相当于没用了
print(dictionary)#<zip object at 0x000002B0767FA980>
dictionary=dict(dictionary)
print(dictionary)
print(max(dictionary))#输出的是key
del dictionary
#dictionary=dict(1='dog',2='cat',3='apple')是错误的，使用dict赋值创建字典要求key为标识符,所以也不需要引号
#dictionary=dict(dog=1,cat=2,apple=3)是正确的
#字典元素的访问与遍历：
#访问——d[key]  d.get(key),二者的区别在于，如果key不存在，前者报错，后者给默认值None
#遍历——for item in d.items   for key,value in d.items
dictionary=dict(dog=1,cat=2,apple=3)
print(dictionary['apple'],dictionary.get('apple'),dictionary.get('zoo'))#注意引号
for item in dictionary.items():
    print(item,end=" ")#得到键值对的元组
print()
for key,value in dictionary.items():
    print(key,value,end=" ")
print()
#字典的一些操作方法
print(dictionary.keys(),dictionary.values())#提取出key/value作dict_xx
print(dictionary.items())#转为键值对
print(dictionary.pop('apple'),dictionary)#取出并删除特定key对应的元素
print(dictionary.popitem(),dictionary)#随机删除
#字典生成式：name={key:value for ... in range()}  name={key:value for key,value in zip(lst1,lst2)}
import random
dictionary={item:random.randint(1,100) for item in range(1,4)}
print(dictionary)
dictionary={key:value for key,value in zip(lst,lst2)}
print(dictionary)

#集合:python中的集合概念和数学中的集合相同，满足互异、无序性
#用{}定义，只能存储不可变数据类型，但是其本身是可变数据类型
#也可以用set去创建集合,set() 函数接受一个可迭代对象作为参数，而不是独立的元素。
collection={1,('hello',9)}
print(collection,type(collection))
collection=set([1,('hello',9)])
print(collection,type(collection))
#集合的操作符：&（交），|（并），-（差：只属于其中一个），^（补）
collection=set([1,2,3])
gather=set([1,5,6])
print(collection&gather,collection|gather,collection-gather,collection^gather)
#集合的增删改
#print(collection.add(9),collection.remove(2))print(collection.clear())是错误的，因为是在原集合上操作
collection.add(9)
collection.remove(2)
print(collection)
for item in collection:
    print(item,end=" ")
print()
for index,item in enumerate(collection,start=1):
    print(index,'->',item,sep='',end="  ")
print()
collection.clear()
print(collection,type(collection))#set() <class 'set'>