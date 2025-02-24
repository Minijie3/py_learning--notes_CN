#字符串是序列的一种，是不可变数据类型

#字符串常用操作：
#string.lower()：字母全转为小写
#string.upper()：字母全转为大写
#string.split(sep=None)：按照一个字符分割字符串，返回一个列表
#string.count(s)：数一下有多少s
#string.find(s)：找s，找到了返回s首次出现的索引，没有找到返回-1，s=子串
#string.index(s)：和find一样，区别在于没有找到s就会报错
#string.starswitch/endswitch(s)：检查是否以s开头/结尾
#string.replace(old,new):用new替换old
#string.center(width,fillchar):在指定宽度范围内居中并用fillchar填充
#string.join(iter):在iter(可迭代对象)中的每个元素之间都加上string，返回的是string
#string.strip(chars):从string中去掉左侧和右侧的chars
#string.lstrip(chars):去左侧
#string.rstrip(chars):去右侧(strip去除字符与字符的排列顺序无关)
strings='dl-sunhaoyu is a hapi-ld'
print(strings.lower())
print(strings.upper())
print(strings.split(sep=" "))
print(strings.count('s'),strings.find('s'),strings.find('v'))
print(strings.startswith('sun'),strings.endswith('sun'))
print(strings.replace('s','v'))
print(strings.center(30,'*'))
print(strings.join(["hello","world"]))
print(strings.strip('ld'),strings.lstrip('ld'),strings.rstrip('ld'))
#格式化字符串：格式化的目的是让字符串能够和其他变量连接而不报错
#1.占位符%s，和C语言一模一样
name='sunhaoyu'
age=99874561111
score=0.5987
print("name:%s,age:%d,score:%.1lf"%(name,age,score))
#2.f-string：f'...{string}...'
print(f'name:{name},age:{age},score:{score}')
#3.format函数格式化
print('name:{0},age:{1},score:{2}'.format(name,age,score))#format中参数按照0，1，2...排
#还可写成：print('name:{2},age:{0},score:{1}'.format(age,score,name))
#格式化控制的详细格式
#冒号：引导符，数字后
#填充：用于填充单个字符
#对齐方式：<左对齐，>右对齐，^居中对齐
#数字：宽度
#，：数字的千位分隔符,只用于整数和浮点型
#.精度：小数点后几位
#？%：形式
print('{0:*^20}---{1:,}'.format(name,age))
print('{0:.5}'.format(name))
print('{0:b},{0:o},{0:x}'.format(age))
print('{0:020}'.format(age))#以20宽度右对齐不足补0
print('{0:0^20}'.format(age))
#<,>,^后面的宽度如果小于要输出的东西的宽度，不会删去多出宽度的内容，这和.不一样
print('{0:.2},{0:.2%},{0:.2E},{0:.2e}'.format(score))
#字符串的编码和解码：str->bytes->str
#编码：str.encode(encoding='?',errors='strict/ignore/replace')#replace是用？替代无法转化的字符
#解码：decode,同上,还有一种bytes的方法见下
name='孙浩宇'
b_name=name.encode(encoding='utf-8',errors='replace')
print(b_name)#b'\xe5\xad\x99\xe6\xb5\xa9\xe5\xae\x87'
print(b_name.decode('utf-8','replace'))
print(bytes.decode(b_name,'utf-8','replace'))
#数据的验证：
#string.isdigit/isnumeric/isalpha/isalnum/islower/isupper/istitle/isspace
#判断字符串是否全是阿拉伯数字/全是数字，可识别中文的一二三四...及罗马数字
#/全是字母（包括中文）/全是数字或字母（包括中文）/全是小写/全是大写/全是首字母大写/全是空格
test1='ⅠⅡⅢⅣ'
test2='Ni.Shi'
test3='你好'
test4='HELLO你好'
test5='hello你好'
print(test1.isnumeric(),test1.isdigit())
print(test2.istitle())
print(test3.isalpha(),test3.islower(),test3.isupper())#纯中文既不是大写也不是小写
print(test4.islower(),test4.isupper())
print(test5.islower(),test5.isupper())#中英文混合中文不作讨论
print("\n".isspace(),bool('\n'))#True
#字符串的拼接：
#1.+
#'?'.join([s1,s2,...])，join的参数是一个可迭代对象
#直接拼接，直接写一起
#格式化
print(''.join(['hello','world']))
print('hello''world')
print('%s%s'%('hello','world'))
print('{0}{1}'.format('hello','world'))
#字符串的去重：
mess='helloworldhelloworldheelstephencurry'
#创造新字符串,for+not in/索引+not in
new=''
for item in mess:
    if item not in new:
        new+=item
print(new)
#利用集合的互异性，集合+排序去重
mess=''.join(sorted(set(mess), key=mess.index))
print(mess)

#正则表达式：

#元字符：具有特殊意义的专用字符，^,&分别表示匹配的开始和结束
#.：匹配任意字符，\n除外
#\w：匹配字母数字下划线
#\W：匹配非字母数字下划线
#\s：匹配任意空白字符
#\S：匹配任意非空白字符
#\d：匹配任意十进制数

#限定符：用于限定匹配的次数
#?:0/1
#+:1/多
#*：0/多
#{n}：n次
#{n,}：n+次
#{n,m}：n~m次，包含m，n
#[]:匹配中括号里面的字符，注意[\u4e00-\u9fa5]匹配任意一个汉字
#^:匹配不在[]里面的字符，如[^0-9]即匹配除0，1，2，...9外的字符
#|:匹配其左右任意的字符，如\d{15}|\d{18}匹配15/18位身份证号
#转义字符：就是转义字符的作用
#分组():改变限定符的作用，如(six|eigh)th，匹配|左右的sixth或eighth

#re模块：python的内置模块,用于使用正则表达式,使用前要import
import re
#re.match(pattern,string,flag=0),pattern是匹配模式,string是待匹配字符串,flag是规则参数
#match用于从待匹配字符串开始，对第一个字符进行匹配，成功返回match对象，失败返回None
pattern='\d\.\d+'
strings='I study python 3.11 every day'
strings2='3.11 I study python every day'
match=re.match(pattern,strings,re.I)#re.I表示忽略大小写
print(match)#None,可见match只匹配开头
match=re.match(pattern,strings2,re.I)
print(match)#<re.Match object; span=(0, 4), match='3.11'>,(0,4)是位置
print(match.start(),match.end(),match.span(),match.group(),match.string)
#re.search():在整个string中查找,返回类型和match相同
match=re.search(pattern,strings,re.I)
print(match,match.group())#group只返回找到的首个
#re.findall(),找出所有匹配到的group并返回列表，这个最常用
match=re.findall(pattern,strings+strings2,re.I)
print(match)
#re.sub()：对指定字符串进行替换，比如替换掉一些机密等等
pattern='HITsz|中国科学院物理研究所'
strings='近期HITsz联合中国科学院物理研究所和国内某科研单位研发了一款新型...'
new_strings=re.sub(pattern,'*'*(len(re.search(pattern,strings,re.I).group())),strings)
print(new_strings)
#re.split():用于对字符串进行分割，返回列表
strings='https://www.baidu.com/s?tn=44004473_8_oem_dg&ie=utf-8&'
pattern='[?&:.]'# ='?|$|:|\.'
match=re.split(pattern,strings)
print(match)
strings='@sunhaoyu   @danhuangpai@xiaogangheacan'
pattern=r'\s*@'#这里的r不影响元字符
match=re.split(pattern,strings)#开头分割出了一个空格，也作为了列表的一个元素
print(match)