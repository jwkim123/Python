# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 14:09:09 2020
@author: jk
"""
재귀 알고리즘
#%%
#함수내에서 다른 함수를 호출하는 예제
def hap(a,b):
    return a+b

def gob(a,b):
    return a*b

def hap_gob(a,b):
    k=hap(a,b)
    m=gob(a,b)
    return k+m

print(hap_gob(2,3))

#%%
#Q.숫자를 입력하면 1부터 해당 숫자까지의 합을 출력하는 함수를 생성하시오
def add_func(a):
    cnt=0
    for i in range(a+1):
        cnt=cnt+i
    return cnt

print(add_func(5))

#%%
#Q.위의 add_func 함수를 재귀함수로 구현하시오
def add_func(a):
    if a==0:
        return 0
    else:
        return a + add_func(a-1)
    
print(add_func(5))

#%%
#Q.팩토리얼 함수를 생성하시오
def factorial(a):
    if a==1:
        return 1
    else: 
        return a*factorial(a-1)
    
print(factorial(5))

#%%
#Q.팩토리얼 함수를 재귀를 이용하지말고 for loop 문으로 구현하시오
def factorial(a):
    cnt=1
    for i in range(1,a+1):
        cnt=cnt*i
    return cnt

print(factorial(5))

#%%
#Q.오라클의 power 함수를 파이썬으로 구현하시오 (loop문으로)
def power(a,b):
    cnt=1
    for i in range(1,b+1):
        cnt=cnt*a
    return cnt
    
print(power(2,3))

#%%
#Q.위의 power 함수를 재귀함수로 구현하시오
def power(a,b):
    if b==0: #재귀를 종료시키는 코드
        return 1
    else:
        return a*power(a,b-1)
    
print(power(2,3))

#%%
#Q.구구단 2단을 만드는 함수를 생성하시오
def multi_table_2dan(a):
    for i in range(1,a+1):
        print('2 x ',i,'=',2*i)
        
print(multi_table_2dan(9))

#%%
#Q.구구단 2단을 재귀함수로 출력하시오
def gugudan2(num):
    if num==0:
        return 1
    else:
        print ('2 x {} = {}'.format(10-num,2*(10-num)))
        return gugudan2(num-1)
    
print(gugudan2(9))
#%%
#Q.두 수를 입력받고 최대공약수를 출력하시오
def gcd(a,b):
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            return i
            
print(gcd(16,24))

#%%
#Q.최대공약수 함수를 재귀로 구현하시오
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
            
print(gcd(16,24))      

#%%
#Q.최대공약수 함수를 재귀로 구현하시오 ver2
def gcd(a,b):
    c=a%b
    if c!=0:
        c=a%b
        return gcd(b,c)
    else:
        return b
print(gcd(16,24))
