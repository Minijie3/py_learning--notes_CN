#程序的描述方式
#自然语言：IPO
#流程图
#伪代码：介于代码与编程语言之间，比较小的程序可用

#顺序结构
#分支结构：if ex:      (换行)else:
#python中没有：？的三目运算符，是由if else来解决的
#python的else if写为elif
x=5
y=10
min=x if x<y else y
#选择结构：py的选择结构不是switch而是match
#循环结构：也差不多
#for：for * in *
#range函数：左闭右开
#range(8)=range(0,8)
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"x",j,"=",i*j,sep='',end="\t")
    print()
#for-else:else后的语句只有for正常循环完（没有break等）才会执行
ID='孙浩宇'
PASSWORD=123456
for i in range(1,4):
    if input("账户：")==ID and eval(input("密码："))==PASSWORD:
        print("成功登录")
        break
    else:
        print("错误，请重来，你还有",3-i,"次机会")
else:
    print("无法登录")
#while:和C一样，写的不同
#break，continue和C一样
#上述都和C类语言一样，只不过语言上的描述不同

#pass关键字：相当于C中的空{}
if True:
    pass

#python的随机生成
import random
number=random.randint(1,100)
print(number)