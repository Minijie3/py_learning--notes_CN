#python中Bug的由来（一只飞蛾）及分类
#语法错误造成的错误
#思路混杂造成的错误
#用户输入错误导致崩溃

#python中的异常处理机制：
#try（可能有异常的代码）except（出现异常的代码）,越大的异常类型越往后放
#无非就是一种if..else..只不过换了个包装
#try(可能会出现异常的)except(出现异常时)else(不出现异常时)(finally(出不出现异常都执行))
try:
    num=eval(input("被除数："))
    by_num=eval(input("除数："))
    result=num/by_num
    #注意这里的除法运算不能放到else里面，因为except检测的是try中的代码有没有问题，如果放到else中，即使by_num=0
    #依然会进行除法，得到的就是报错。这样还会造成输入非数字时，起作用的实际上只有BaseException，因为检测出来的是
    #eval的使用错误而不是除法的值类型错误。
except ZeroDivisionError:
    print('除数为0')
except ValueError:#在python中没有char的概念，所以没有char转int
    print('请输入数字')
except BaseException:
    print('请输入数字。')
else:
    print(result)
finally:
    print('任务结束')

#raise关键字：抛出(不是输出)一个异常，提醒程序出现了错误以正确处理。raise Expression(异常信息描述)
try:
    gender=input('请输入性别：')
    if gender!='男' and gender!='女' and gender!='孙浩宇':
        raise Exception('请输入男/女')
    elif gender=='孙浩宇':
        raise Exception('世界确实是一个巨大的孙浩宇')
    else:
        print('OK')
except Exception as e:
    print(e)

#python中常见的异常类型：
#ZeroDivisionError：除数为0
#IndexError：超出索引范围
#KeyError：字典取值时key不存在
#NameError：变量不存在
#SyntaxError：python语法错误
#ValueError：传入的值错误
#AttributeError：属性/方法异常
i=10
try:
    print(i.name)
except AttributeError:
    print('AttributeError')
#BasedException：最大的异常范围
#TypeError：类型不合适引起的异常,比如string+int
#IndatationError：缩进错误引发的异常，比如单独的print不顶格写

#pycharm调试：
#断点：单击有效代码行
#进入调试窗口：debug
#按窗口调试