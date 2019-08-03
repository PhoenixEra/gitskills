'''
def bmi(h,w):
	BMI = w/(h*h)
	if BMI > 32:
		print("严重")
	elif BMI > 28:
		print("肥胖")
	elif BMI > 25:
		print("过重")
	elif BMI > 18.5:
		print("正常")
	else:
		print("过轻")
	return BMI

h = 1.75
w = 80.5
c = bmi(h,w)
print(c)

def add(c):
	c = c + 10
	return c

c = 10
add(c)




L = ['Bart', 'Lisa', 'Adam']
for name in L:
	print('Hello, '+name+'!')


K = ['Barty', 'Lisa', 'Adam','Cathy']
for name in K:
	print('Hello,' + name + '!')
	



n1=255
n2=1000
print(str(hex(n1)))
print(type(str(hex(n1))))
print(str(hex(n2)))
print(type(str(hex(n2))))


def abc(x,y,z=123):
	return x+y+z

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


my_abs('90')

import math
def quadratic(a,b,c):
	x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
	x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
	return x1,x2
	
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:



def product(*y):
	if not y:
		print('error')
	else:
		p = 1
		for i in y:
			p = p * i
		return p

a = product(3,4,5,6)
print(a)

b = product()
print(b)

def is_leap_year(y):
	return y%4==0 and ( y%100!=0 or y%400==0 )


yy = input('请输入年：xxxx')
y = int(yy)
mm = input('请输入月：mm')
m = int(mm)
dd = input('请输入日：dd')
d = int(dd)

leap_year_num = 0
for i in range(1990,y):
	if is_leap_year(i):
		leap_year_num = leap_year_num + 1
days_y = (y-1990) * 365 + leap_year_num

months = [31,28+is_leap_year(y),31,30,31,30,31,31,30,31,30,31]

days_m = 0
for j in range(m-1):
	days_m= days_m+months[j]

days= days_y+days_m+d

week = ['日','一','二','三','四','五','六']
print('星期'+week[days%7])

def hanoi(n,a,b,c):
	if n==1:
		print(a,'--->',c)
		return 1
	else:
		s1= hanoi(n-1,a,c,b)
		s2= hanoi(1,a,b,c)
		s3= hanoi(n-1,b,a,c)
		return s1+s2+s3

print(hanoi(3,1,2,3))

def hanoi(n):
	if n==1:
		return 1 
	else:
		return 2*hanoi(n-1)+1


#打印1-99奇数
a= range(100)	
for i in a:
	if i%2 !=0:
	else:
		pass



#构造坐标1-99列表：
L=[(i,j) for i in range(100) if i%2==1  for j in range(100) if j%2==1]
print(L)

def trim(s):
	cnt1=0
	for i in s:
		if i== ' ':
			cnt1 = cnt1+1
		else:
			break
	cnt2=0
	for i in s[-1::-1]:
		if i == ' ':
			cnt2 = cnt2+1
		else:
			break

	return s[cnt1:len(s)-cnt2]

lj=trim('   ttyy1314   ')

if trim('hello  ') != 'hello':
    print('测试失败1')
elif trim('  hello') != 'hello':
    print('测试失败2')
elif trim('  hello  ') != 'hello':
    print('测试失败3')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4')
elif trim('') != '':
    print('测试失败5')
elif trim('    ') != '':
    print('测试失败6')
else:
    print('测试成功')
print(lj)

d = {'a': 1, 'b': 2, 'c': 3}
for a,b in d.items():
	print(a,'=',b)

for c in 'ttyy1314':
	print(c)



def findMinAndMax(A):
	if not A:
		return (None,None)
	a = A[0]
	b = A[0]
	for i in A:
		if a > i:
			a = i
		if b < i:
			b = i
	return (a,b)



# 返回列表L的平均数
def MiddleNum(L):
	s = 0
	for i in L:
		s = s + i
	return s / len(L)
	


print(MiddleNum([1,2,3,4,5]))

# 返回列表L的平均数
import numpy as np
def MiddleNum(K):
	J = np.array(K)
	J.sort()
	return (J[int((len(J)-1)/2)]+J[int(len(J)/2)])/2

print(MiddleNum([3,2,5,7,6]))

'''

# 1.可以从控制台连续输入数字，当输入的数字为0时不可以再输入
''' 
hint: input() 死循环
'''

# 2.任意输入一个整数（小于10位），求它一共有多少位
'''
hint: 不断/10求商，直到...退出循环
'''

# 3.一张纸的厚度大约是0.08mm，对折多少次之后能达到珠穆朗玛峰的高度（8848.13米）
'''
hint: 不断...直到...
'''

