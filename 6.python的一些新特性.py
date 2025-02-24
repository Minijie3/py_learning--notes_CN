#1.模式匹配：说白了就是C中的switch case，在python里变成了match
infomation=eval(input('选英雄：'))#这里涉及到输入字典，结合eval
#所有的input和eval的正确使用与正确输入都是建立在对eval的深刻理解上的
#输入dict(Minijie3=18)也是正确的
match infomation:
    case {"孙浩宇":88}:
        print("不太聪明")
    case {"Minijie3":18}:
        print('孙浩宇的爸爸')
    case _:#相当于C里面的default
        print('谁啊')

#2.字典合并运算：|（类似集合里面的|）
dictionary1=dict(dog=1,cat=2)
dictionary2=dict(zoo=3,sunhaoyu=4)
print(dictionary1|dictionary2)

#3.同步迭代:
#可迭代对象（iterable）是指能够被迭代遍历的对象
#例如列表（list）、元组（tuple）、集合（set）、字典（dictionary）
#以及字符串（string）等。此外，还包括自定义的类对象
#同步迭代（Synchronized Iteration）是指同时遍历多个可迭代对象的方式。
#当我们有多个可迭代对象，且想要按照相同的索引位置逐个获取各个可迭代对象的元素时，可以使用同步迭代来实现。
fruit=['apple','banana','sunhaoyu']
count=[1, 2, 3]
for key,value in zip(fruit,count):
    match key,value:
        case 'apple',1:
            print("一个苹果")
        case 'banana',2:
            print("两个香蕉")
        case 'sunhaoyu',3:
            print("三个儿子")