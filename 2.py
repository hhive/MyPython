#if condition:
#	do something
#else:
#	do otherthing
total = 32.5
is_vip = True

if total > 50:
	if is_vip:
		discount = 0.8
	else:
		discount = 0.9
elif total > 30:
	discount = 0.9
else:
	discount = 1

total *= discount

print("total price{}￥".format(total))
#条件判断可以任意组合
#elif可以有任意多个，else可有可无
#条件判断可以嵌套
print(bool(''),bool({}),bool([]))#一个bool值，概念上更像是有和无的区别
#and,or,not
a = True
b = False
print('a and b is {}'.format(a and b))
a = 'hello world'
b = [1,2,3]
print('a and b is {}'.format(a and b))#先进行a的，再进行b的才能判断
print('a or b is {}'.format(a or b))#判断了a的已经确定了，不进行b的检测
b = []
print('a and b is {}'.format(a and b))
#assert断言，断定某种情况，如果不是程序就崩溃，用于debug
#assert a == 18 ,'她竟然不是18岁'
#for循环
fruits = ['banana','apple','mango']
for fruit in fruits:
	print ('当前水果：',fruit)

for index in range(0,1):#len(fruits)
	print('当前水果：',fruits[index])

#for else
for num in range(10,15):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print('%d 等于 %d * %d' % (num,i,j))
         break            # if语句的一部分，执行完if就跳出当前循环及回到上一级for循环
   else:                  # 循环的 else 部分
      print (num, '是一个质数')

#while
nums = [12,37,5,42,8,3]
even = []
odd = []
while len(nums)> 0:
	num = nums.pop()
	if(0 == num%2):
		even.append(num)
	else:
		odd.append(num)

print(even)
print(odd)