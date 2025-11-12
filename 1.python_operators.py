'''
Python Operators
------------------
'''

#1.ARITHEMATIC OPERATORS
a=20
b=10
print("a+b:",a+b) #a+b: 30
print("a-b:",a-b) #a-b: 10
print("a*b:",a*b) #a*b: 200
print("a/b:",a/b) #a/b: 2
print("a//b:",a//b) #a//b: 2
print("a**b:",a**b) #a**b: 10240000000000

#2. Comparision Operators
c=30
d=40
print('c<d:',c<d) #c<d: True
print('c>d:',c>d) #c>d: False
print('c<=d:',c<=d) #c<=d: True
print('c>=d:',c>=d) #c>=d: False
print('c==d:',c==d) #c==d: False
print('c!=d:',c!=d) #c!=d: True

#3. Assignment Operators
'''
var = var op val
var op= val
'''
e=100
e+=100
print('e+=100:',e)
e==100
print('e-=100:',e)
e*=100
print('e*=100:',e)
e//=100
print('e//=100:',e)
e**=100
print('e**=10:',e)
e%=3
print('e%=10:',e)
e/=5
print('e/=5:',e)

#4.logical operators
x=100
y=50
print("x%20==0 and y%20==0:",x%20==0 and y%20==0)
print("x%20==0 or y%20==0:",x%20==0 or y%20==0)
print("not x%20==0:",not x%20==0)
print("not y%20==0:",not y%20==0)


#5.Membership operators (in and not)
s='python programming'
print("'i' in s:",'i' in s)
print("'x' not in s:",'x' not in s)

l=[1,2,3,4,5]
print("3 in l:",3 in l)
print("10 not in l:",10 not in l)

t=(102,103,104,105)
print("108 in t:",108 in t)
print("104 not in l:",104 not in t)

s={10,20,30,40}
print("40 in s:",40 in s)
print("50 not in s:",50 not in s)


d={1:1,2:4,3:9,4:16,5:25}
print('1 in d:',1 in d)
print('4 not in d:',4 not in d)

#6. identity operators
a=[1,2,3,4]
b=[1,2,3,4]
print('a is b:',a is b)
c=a
print('a is c:',a is c)
print('id(a):',id(a))
print('id(b):',id(b))
print('id(c):',id(c))

print('a is not b:',a is not b)
print('a is not c:',a is not c)

#Bitwise operators
print('4&5:',4&5)
print('11|12:',11|12)
print('14^15:',14^15)
print('~16:',~16)
print('8<<1:',8<<1)
print('16>>1:',16>>1)







      
