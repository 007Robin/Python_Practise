#!/usr/bin/env python
#coding=utf-8

'''
1. keyboard input sth...
'''
name = raw_input("what's your name? ") 
age = raw_input("How old are you? ")

print "Your name is :", name
print "you are " + age + " years old"

aften_ten = int(age) + 10
print "you are " + str(aften_ten) + " years old"


'''
2. 由 r 开头引起的字符串，就是原始字符串，在里面放任何字符都表示该字符的原始含义。
'''
dos = r"c:\www.apple.com"  



'''
3. 切片 str[:]  [x1, xn) 左闭右开
c = str[:] 和 c = str, 如同复制，但其实没有生成新字符串，类似于&
'''
s = "learn python"
c = s[2:100]
print c
print id(c)

'''same memory address as s'''
d = s[:]
print id(d)
e = s
print id(e)

'''
4. String 操作有：
+ 				拼接
in 				判断字符串是否在另一个字符串内
max() min()
cmp(str1, str2) 0相等 -1小于 1大于 从第0位开始依次比较 返回结果
ord('a')  		转换成ASCII码
chr(97)			ASCII数转成字符
str*10			重复10次str
len(str)			字符串长度
'''

'''
5. 格式化3种方法：
占位符
%s	str()字符串
%r	repr()字符串
%d	十进制整数
%c	单个字符
%b	二进制整数
%i	十进制整数
%o	八进制整数
%x	十六进制整数
%e	指数 (基底写为 e)
%E	指数 (基底写为 E)
%f	浮点数 %.2f  %+.2f
%F	浮点数，与上相同
%g	指数(e)指数 或浮点数 (根据显示长度)
%G	指数(E)或浮点数 (根据显示长度)

python提倡
{}占位符 
string.format()格式化的方法

字典格式化
%(sth)s  
 "stribalabala %(sth)s" % {"sth":s}
'''

print "Suzhou is more than {year} years. {name} lives in here.".format(year=2500, name="Xin")

s = "python"
print "I love %(sth)s" % {"sth":s}

'''
dir(str) 查看使用
help(str.xxx)

str转化为list:
str.split(" ") 以空格分割, 返回list值
str.split("."|" ") 以.和 分割, 可用 | 或许多符号，注意有些符号需转义。
str.split()    如果split()不输入任何参数，就是见到任何分割符号，就用其分割了。
str.split(".", maxsplit) 最多完成maxsplit次分割
str2 = re.split(r"\W+", str)  re.split的比split更强大，只保留字母数字
'''
a = "www.baidu.com"
print a.split(".")
b = "I love you"
print b.split(" ")

word_list = [x for x in word_list if not (x.isdigit() or any(char.isdigit() for char in x))]
#可用于删除所有数字，和含数字的str

'''
S.strip() 去掉字符串的左右空格
S.lstrip() 去掉字符串的左边空格
S.rstrip() 去掉字符串的右边空格
原来的值没有变化，而是新返回了一个结果
'''
b = " hello "
print b.strip()
print b

'''
S.upper() #S 中的字母大写
S.lower() #S 中的字母小写
S.capitalize() # 首字母大写
S.title() #每个单词的第一个字母变为大写
S.isupper() #S 中的字母是否全是大写
S.islower() #S 中的字母是否全是小写
S.istitle() #判断每个单词的第一个字母是否为大写 "I Love You"为true
'''

'''
join是split的逆运算 "[sep]".join(list)
join实现拼接 不能+的时候，如list拼接
list = ["self","as","begin"]
"*".join(lst)	用*拼
".".join(lst)	用.拼
"".join(lst)	没有连接符，表示一个一个紧邻着
'''
s = "I am, reading\npython\tbook on line"
print s
print s.split()
print " ".join(s.split())

'''
unicode编码问题：
先用b = a.decode()解码转换成unicode
在用c = b.encode('utf-8')解码成原来类型

中文问题
1.开头声明
# -*- coding: utf-8 -*-
# coding:utf-8
2.遇到字符串字节串立刻转化为unicode
unicode_str = unicode('中文', encoding='utf-8')
print unicode_str.encode('utf-8')
打开文件用codecs.open
import codecs
codecs.open('filename', encoding='utf8')
'''

'''
list str 序列型，用法类似. list可变,可修改，str不可变,新生成
[a:b] 切片[a,b)  一定要注意，左<右, [-3,-1)合法, [-1, -3]非法
[]索引 0左一，1左一，2/ -1右边第一 -2右二 -3
反转 [::-1] / list(reversed(lst/"abcd")
len()	长度
+ 		连接,重新生成一个新的
* 		重复
in		元素在list里吗
max() min()
cmp()
a.append("abc"/123) <=> a[len(a):] = ["abc"/123] 追加元素(整体追加），原地修改，无返回值
a.extend(L) <=> a[len(a):] = L 追加list，个体追加
a.extend(str) str被以字符为单位拆开,追加a后，extend()需要参数是iterable类型的,无返回值
hasattr(xxx,'__iter__') 用于判断xxx是否是iterable的，可迭代的
列表是可以修改的append() / extend()。这种修改，不是复制一个新的，而是在原地进行修改。
'''

lst = [1,2,3]
lst2 = lst.append[4,5,6]
print lst2     '''get nothing,because append no return'''
print lst   ''' 1,2,3,[4,5,6]'''

lst = [1,2,3]
lst3 = lst.extend[4,5,6]  ''' nothing, no return'''
print lst   ''' 1,2,3,4,5,6 '''

'''
lst.count(element) 	数element出现几次,没有返回0
lst.index(elemnet)  返回位置，没有则出错
lst.append(x)
lst.extend(L)
lst.insert(i,x) 	x插入到索引值是 i 的元素前面,如果遇到那个 i 已经超过了最大索引值，会自动将所要插入的元素放到列表的尾部，即追加。
lst.remove(x)	删the first item x, 如果x 没有在 list 中，会报错。原地修改
lst.pop([i]) 删i序号处的元素，如果不写，默认删除最后一个，并且将该删掉元素返回
lst.reverse() 原地反过来，不是另外生成一个新的列表。所以，它没有返回值
lst.sort() 列表进行原地修改，没有返回值,默认从小到大lst.sort(reverse = True) 从大到小
lst.sort(key = len)	按以字符串的长度为关键词进行排序
del lst[i]
'''
all_users = ["python","xin","github","python","datiancai"]
print "python" in all_users
if "python" in all_users:
	all_users.remove("python")
	print all_users
else:
	print "'python' is not in all_users"


lst = ["python","jar","juice","heat","basic"]
lst.sort(key = len)
print lst

listoflist = [['',0],['t',24],['e',5],['op',90],['mm',2]]
listoflist.sort(key=lambda x: x[1])
print listoflist
#[['', 0], ['mm', 2], ['e', 5], ['t', 24], ['op', 90]]

'''
tuple 是一种序列类型的数据，这点上跟 list/str 类似。它的特点就是其中的元素不能更改，不可变，它的元素又可以是任何类型的数据。
元组是用圆括号括起来的，其中的元素之间用逗号隔开
如果一个元组中只有一个元素的时候，应该在该元素后面加一个半角的英文逗号。
lst = list(tuple_t)  tuple-->list
tuple_t = tuple(lst) list-->tuple
tuple比list快，写一个老要遍历的const变量集常用tuple；不需修改数据“写保护”；可以在dictionary中被用作key(因key必须是不可变的；用在字符串格式化中

'''

t = 1,"23",[123,"abc"],("python","learn") 
print t
''' 
(1, '23', [123, 'abc'], ('python', 'learn'))
t[0] = 8 , t.append("x") --> EROOR!! 
'''

a = (3)
print type(a)

b = (3.)
print type(b)

'''
进制转换
int() bin() oct() hex()
'''
'''
创建dict
1.
mydict = {}
person = {"name": "xin", "site": "github.io", "language": "python"}
{'name': 'xin', 'language': 'python', 'site': 'github.io'}
key:value key唯一，不能重
增加键值对:
person['name2'] = "wzy"
dict可以原地修改，可变

2.
tuple构建
name = (["first","google"],["second","yahoo"])
website = dict(name)
print website  
{'second': 'Yahoo', 'first': 'Google'}

ad = dict(name = "xin", age = 12)
print ad
{'age': 42, 'name': 'qiwsir'}

3.
使用fromkeys
website = {}.fromkeys(("third","forth"), "facebook")
print website 
{'forth': 'facebook', 'third': 'facebook'}
这种方法是重新建立一个 dict
字典中的“key”，必须是不可变的数据类型；“value”可以是任意数据类型'''
dd = {(1,2) : 1}
print dd
''' dd = {[1,2], 1} ERROR!!! because key is list, list可变 
字典没有顺序，就没有什么索引和切片啦
len(d)，		返回字典(d)中的键值对的数量
d[key]，		返回字典(d)中的键(key)的值
d[key]=value，	将值(value)赋给字典(d)中的键(key), 没有则增加这项
del d[key]，	删除字典(d)的键(key)项（将该键值对删除）
key in d，		检查字典(d)中是否含有键为 key 的项
用字典也可以实现格式化字符串的目的。

'''

city_code = {"suzhou":"0512", "tangshan":"0315", "hangzhou":"0571"}
print "Suzhou is a beautiful city, its area code is %(suzhou)s" % city_code

'''
temp 就是所谓的模板，在双引号所包裹的实质上是一段 HTML 代码。然后在 dict 中写好一些数据，按照模板的要求在相应位置显示对应的数据。
'''
temp = "<html><head><title>%(lang)s<title><body><p>My name is %(name)s.</p></body></head></html>"
my = {"name":"qiwsir", "lang":"python"}
temp % my

'''
关联数组/Associative Array/Map/Dictionary 这种数据结构包含（键，值）的有序对。有序对可以重复（如 C++ 中的 multimap）也可以不重复（如 C++ 中的 map）。
1.向关联数组添加配对
2.从关联数组内删除配对
3.修改关联数组内的配对
4.根据已知的键寻找配对
解决字典问题的常用方法，是利用散列表（Hash table，也叫哈希表),也可以直接使用有地址的数组，或二叉树，和其他结构。

对象有类型，变量无类型,变量其实是一个标签。这种现象普遍存在于 Python 的多种数据类型中。

dict方法：
1.浅copy
a = b 			id(a),id(b) 同一块内存
y = x.copy()	开辟了新内存空间,是基本类型int string的会重新储存，不是基础类型list这些，不会在被复制对象中重新储存，而是引用
id(x[key]) = id(y[key]) 此时value是个list型，key指向同一块内存空间，同一个对象
id(x[key]) = id(y[key]) 此时value是个str型，key指向不同内存空间，不同对象
改变y， 改变x的非内置类型，不改变x的内置类型
y[key].remove(value)	如上，x不会被删内置类型, 会删list型
y[key] = value2			如上，x不会被改内置类型, 会改list型

2.deepcopy
import copy
z = copy.deepcopy(x) 深拷贝了一个新的副本,开辟新内存空间了
改变z，不会改变x

3.clear
dt.clear()		清空
del dt			删了

4.get(..)
dt.get(key)		返回该key的value，没有则返回None，不同于dt[key](dt[key]没有，它会直接Error)
dt.get(key, value2)	该key的value，没有则返回value2

5.setdefault(...)
dt.setdefault(key)	返回该key的value，没有则返回None，且插入None
dt.setdefault(key, value2) 没有，返回value2，且字典里插入key value2

6.items/iteritems
D.items() 		返回pair元组的列表-> list of D's (key, value) pairs, as 2-tuples
D.iteritems()   -> an iterator over the (key, value) items of D 得到的 dd_iter 的类型，是一个'dictionary-itemiterator'类型，不过这种迭代器类型的数据不能直接输出，必须用 list()转换一下，才能看到里面的

7.keys/iterkeys 	同上，获得key的list/key list的iterator
8.values/itervalues	同上，获得value的list/value list的iterator

dd
{'lang': 'Python', 'web': 'www.itdiffer.com', 'name': 'qiwsir'}
dd.keys()
['lang', 'web', 'name']
dd.values()
['Python', 'www.itdiffer.com', 'qiwsir']

9.pop/popitem
list.remove(x)用来删除指定的元素，而 list.pop([i])用于删除指定索引的元素，如果不提供索引值，就默认删除最后一个。

D.pop(k[,d]) -> v, remove specified key and return the corresponding value. If key is not found, d is returned if given, otherwise KeyError is raised

D.popitem() -> (k, v), remove and return some (key, value) pair as a 2-tuple; but raise KeyError if D is empty. 一次只能随机删除一对键值对，并以一个元组的形式返回

10.update
d1.update(d2)	把字典 d2 更新入了 d1 那个字典，于是 d1 中就多了一些内容，把 d2 的内容包含进来了。
d2.update([(k1,v1), (k2,v2)])

11.has_key(...)
D.has_key(k) -> True if D has a key k, else False
k in D
'''
'''
能够索引的，如 list/str，其中的元素可以重复
可变的，如 list/dict，即其中的元素/键值对可以原地修改
不可变的，如 str/int，即不能进行原地修改
无索引序列的，如 dict，即其中的元素（键值对）没有排列顺序

set: 有的可变，有的不可变；元素无次序，不可重复。
tuple 算是 list 和 str 的杂合
set 则可以堪称是 list 和 dict 的杂合.

set() set{} 创建集合 
{}不提倡
无法创建含有 list/dict 元素的 set.

某数据“不可哈希”(unhashable)就是其可变，如 list/dict，都能原地修改，就是 unhashable。否则，不可变的，类似 str 那样不能原地修改，就是 hashable（可哈希）的。

字典，其键key必须是hashable 数据，即不可变的。

set其元素也要是“可哈希”的,试图将字典、列表作为元素的元素，就报错了.
集合没有序列，不能用索引方式对其进行修改。
分别用 list()和 set()能够实现两种数据类型之间的转化。
特别说明，利用 set()建立起来的集合是可变集合，可变集合都是 unhashable 类型的。

set.add(elment)
s1.update(s2)       #把 s2 的元素并入到 s1 中.
b_set.pop()     #从 set 中任意选一个删除,并返回该值,不能指定删除某个元素.pop()不能有参数
set.remove(obj)中的 obj,必须是 set 中的元素,否则就报错.
set.discard(obj)中的 obj 如果是 set 中的元素,就删除,如果不是,就什么也不做,do nothing.
set.clear()


frozenset()
被冻结的集合,不能在原处修改.是 hashable 类型
无add等修改方法

判断集合 A 是否是集合 B 的子集，可以使用 A<B，返回 true 则是子集，否则不是。另外，还可以使用函数 A.issubset(B)判断。
A 是否是 B 的子集 A.issubset(B) <==> B 是否是 A 的超集B.issuperset(A) 。

A、B 的并集: A | B 也可使用函数 A.union(B)
A、B 的交集: A & B 或者 A.intersection(B)
A 相对 B 的差（补）: A - B 或者 A.difference(B) <==> A - AintersectionB
-A、B 的对称差集: A.symmetric_difference(B) <==> AunionB - AintersectionB
'''
'''
A and B，含义是：首先运算 A，如果 A 的值是 true，就计算 B，并将 B 的结果返回做为最终结果
A or B, 如果 A 的值是True, 返回True, 表达式最终结果是True.否则A 的值不是True, 看B 的值，然后就返回B的值做为最终结果。
'''

'''
对应赋值。x,y,z = 1, "a", ["a","b","s"]
交换	a,b = b,a
链式赋值 m = n = "I use python"
m is n 检查两个变量所指向的值是否是同一个,（注意，同一个和相等是有差别的。在编程中，同一个就是 id()的结果一样。

A = Y if X else Z
如果 X 为真，那么就执行 A=Y
如果 X 为假，就执行 A=Z

range(start,stop[, step])
start：开始数值，默认为 0,也就是如果不写这项，就是认为 start=0
stop：结束的数值，必须要写的。
step：变化的步长，默认是 1,也就是不写，就是认为步长为 1。坚决不能为 0

zip()  压缩成一个又tuple型元素构成的list
dict(list) 转成字典
'''

r = [(2,11),(4,12),(6,13)]
print zip(*r)
'''	[(2, 4, 6), (11, 12, 13)]'''

'''
enumerate
'''
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print list(enumerate(seasons))
'''[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')] 
'''
print list(enumerate(seasons, start=1))
'''
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
'''
'''
list解析
squares = [x**2 for x in range(1,10)]
mybag = [' glass',' apple','green leaf ']
[one.strip() for one in mybag]              #去掉元素前后的空格
'''
path = os.path.abspath('.') 	#获取当前绝对路径，需import os

f = open("file.txt")
for line in f:
     print line,
'''	
learn python
http://qiwsir.github.io
qiwsir@gmail.com

open(filename, "w") 写, 如文件存在，则清空该文件，再写入新内容
open(filename, "r") 读
open(filename, "a") 追加，文件指针自动至文件末尾
r+	以读写方式打开文件，可对文件进行读和写操作。
w+	消除文件内容，然后以读写方式打开文件。
a+	以读写方式打开文件，并把文件指针移到文件尾。
b	以二进制模式打开文件，而不是以文本模式。该模式只对 Windows 或 Dos 有效，类 Unix 的文件是用二进制模式进行操作的。
牢记一个事情：file.close()

with open("130.txt","a") as f:

read()
readline()
readlines()

seek()  让指针移动,以字节为单位进行移动
'''

