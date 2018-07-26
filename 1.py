print("Hello World")
print(10 ** (1/3))
import math
print(math.pi)
#a=5,b=10是错的
a=5
b=10
print("a={};b={}".format(a,b))
#交换变量
a,b=b,a
print("a={};b={}".format(a,b))
print(100/3)
#取数
print(round(100/3,3))
#乘方
print(math.pow(3,10))
print(3 ** 10)
#取整
print(math.floor(2.232))
print(math.ceil(2.232))
#度数
math.radians(100)
#商和余数
print(divmod(10,3))
print(100>10)
a="hello"
print(a)
#\转义字符
print('a\'b')
a='Hello'
b='World'
print(a+b)
print(a*3)
print(len(a))
print('hello "world"' )
#取前多少字符
print(a[:2])#a[0:2]
#前五个中每两个字符取一个
print(a[0:5:2])
#取后几个字符
print(a[-3:])#a[-3:最后一个]
#翻转字符
print(a[::-1])
#单字符
print(a[0])
#可以用c的方式输出
print("My name is %s and weight is %d kg!" % ('Zara', 21) )
#居中
print(a.center(10))
print(a.center(10,"#"))
#count,endswith,startswith,find,index,upper,lower,istitle,isupper,islower,
#取出空格或转换符
a='   sdsfvax  \n\t'
print(a.strip())#restrip,swapcase
print(id(a))#字符串函数是生成一个新的字符串进行操作
var = 10
print(type(var))
var = "str"
print(type(var))
var = [1,2,3,"ni hao",[],[100,200]]
var.append("good")
print(var)
print(type(var))
print(var[:2])
#clear
var1 = var
var1[0]=10
print(var1),print(var)
var1 = var.copy()
var1[0]=10
print(var1),print(var)
#浅复制和深复制
var1[-2][0]=999
print(var1),print(var)
print(id(var)),print(id(var1))
print(id(var[-1])),print(id(var1[-1]))
a = [1,2]
b = [3,4]
print(a);
print(a+b)
a.extend(b)#没有返回值，但a变了
print(a)
a.insert(1,100)
print(a)
print(a.pop())
print(a)
#remove,sort
a.sort(reverse=True)
print(a)
print(2 in a)
print("Hello World")
a = 'str'
print(a.center(20))
#元组
var = (1,2,1,3,4,5,[23,34,43])
var.count(1)
#输出1的个数
print(var.count(1))
print(a)
#字典
var={
	'z':100,
	'y':200
}
print(var['z'])
print(var)
words = ['z','y']
location = [100,200]
#拉锁函数，将两个列表拉成一个列表
print(zip(words,location))
print(list(zip(words,location)))
#转换成字典
print(dict(list(zip(words,location))))
print(list(zip([1,2],[3,4],[4,5])))
print(list(zip([1,2],[3,4],[4,5,5])))
a,b=1,2
print(a),print(b)
#dict
students = ['one','two','sun','zhao','qian']
money=dict.fromkeys(students,10)
print(money)
print(money['one'])
print(money.get('one'))
a = money.get('ww')
print(a)
#get可以直接给不存在的元素赋值
a = money.get('ww',10)
print(a)
print(money.keys(),money.values())
#整合成一个列表
print(money.items())
#删除字典元素
print(money.pop('zhao'))#输出对应的值
print(money)
money['zhao'] = 100#必须赋值
print(money)
print(money.setdefault('two',1000))#返回原始值,如果不存在就赋值并返回赋的值
print(money.setdefault('haha',1000))
import this

