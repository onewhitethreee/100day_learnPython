import pysnooper
from random import randint

'''def fac(num):
    result = 1
    for n in range(1,num+1):
        result *= n
    return result
m = int(input('m = '))
n = int(input('n = '))
print(fac(m) // fac(n) // fac(m-n))'''


'''@pysnooper.snoop()
def roll_dice(n=1):#执行的次数
    total = 0
    for i in range(n):#按照次数来取得随机数
        total = randint(1,6)
    return total
#print(roll_dice())#打印随机数
# 摇三颗色子
print(roll_dice(3))#修改为三次'''

'''@pysnooper.snoop()
def add(*args):#*args代表为可变参数
    return a + b + c
#print(add())#打印为0
#print(add(1))#打印为1
print(add(1, 2))#打印为3
print(add(1, 2, 3))#打印为6'''
