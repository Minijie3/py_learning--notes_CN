# coding=utf-8
#中文文档声明注释一定要写在第一行，可以去文件那里打开看看编码方式，就会是utf-8

#Minijie3
#特别鸣谢我的某位不愿意透露姓名的好友（er zi）承担了我许多的标识符

#python和C，C++不同，不是编译语言，是解释类型的编程语言

'''
哈咯哈咯喂喂
说话说话
'''
#只因你太美
def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    #python采用严格的缩进来表示程序逻辑
    """
    print(money)(和下面对照一下，颜色不影响它的注释身份)
    上下单双引号要一致
    """
    #money = 50
    #print("孙浩宇全身只有", money, "元")
    #print("孙浩宇是坏厚米")
    #print('''孙浩宇是坏厚米''')
    #print("""**""")
    #print('**')
#print(value,sep=' ',end='\n',file=None)
#写入file前要用fp=open(file,way)，注意与C语言的fopen区分
#写入后要用fp.close（）,注意与C语言的fclose（fp）; 区分
    print(chr(98),ord('b'),chr(21271))
    print(18,52,66,sep='$',end='->')
    print('heiheihei'+'sunhaoyu')
    name=input("请选择你的英雄：")
#varible=input(tips)
    #python中变量存在类型，但是不用声明类型即可定义
    print("获得新英雄："+name)
    number=int(input("请输入英雄的年龄："))
    #强制类型转换与C类语言区别开
    if number == 18:
        print("woo! 刚满十八岁~~")
    else:
        print("woo!")