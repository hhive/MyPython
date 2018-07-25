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