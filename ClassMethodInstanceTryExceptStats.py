# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 09:43:20 2020
@author: jw
"""
#%%
#Q.총을 만드는 클래스를 작성하고 총을 생성하면 "총이 만들어졌습니다. 총알은 0발 장전되었습니다."
#라는 메세지가 출력되게 총 클래스를 만드시오
class Gun():
    def __init__(self):
        self.bullet=0
        print('총이 만들어졌습니다. 총알은 %d 발 장전되었습니다.' %(self.bullet))

yys_gun1=Gun()

#%%
#Q.카드 클래스를 만들고 충전한 금액보다 더 많은 금액을 소비하면 어떻게 되는지 테스트하시오
class Card(): 
    def __init__(self):
        self.cash=0
        print('카드가 발급되었습니다.')
    def charge(self,num):
        self.cash += num
        print('%d원이 충전되었습니다.' %(num))
    def consume(self,num):
        if self.cash>=num:   #잔액이 소비하는 돈보다 커야지만 쓸수있게
            self.cash-=num
            print('%d원이 사용되었습니다.' %(num))
        else: 
            print('잔액이 부족합니다.')

yys_card1=Card()
yys_card1.charge(10000)
yys_card1.consume(18000)

#%%
#Q.팀장님의 Card 클래스를 상속받으시오
class Card(): #부모클래스
    def __init__(self):
        self.cash=0
        print('카드가 발급되었습니다.')
    def charge(self,num):
        self.cash += num
        print('%d원이 충전되었습니다.' %(num))
    def consume(self,num):
        if self.cash>=num:   #잔액이 소비하는 돈보다 커야지만 쓸수있게
            self.cash-=num
            print('%d원이 사용되었습니다.' %(num))
        else: 
            print('잔액이 부족합니다.')

class Movie_Card(Card): #내 클래스이름(무보클래스인 상속받은 클래스이름)
    pass #아무것도 코딩하지 않을거라는 뜻

m_card1=Movie_Card()
m_card1.charge(10000)
m_card1.consume(8000)

#%%
#Q.팀장님의 Card 클래스를 상속받아 영화관할인이 되게 구현하시오
#부모클래스
class Card(): 
    def __init__(self):
        self.cash=0
        print('카드가 발급되었습니다.')
    def charge(self,num):
        self.cash += num
        print('%d원이 충전되었습니다.' %(num))
    def consume(self,num):
        if self.cash>=num:   #잔액이 소비하는 돈보다 커야지만 쓸수있게
            self.cash-=num
            print('%d원이 사용되었습니다.' %(num))
        else: 
            print('잔액이 부족합니다.')

#자식클래스
class Movie_Card(Card): #내 클래스이름(무보클래스인 상속받은 클래스이름)
    def consume(self,num,place): #부모클래스의 consume을 내 consume으로 덮어쓰기(overriding)
        if place in ('영화관','주유소'):
            num=0.8*num
            if self.cash>=num: #잔액이 num보다 크다면 카드를 사용하고 아니면 잔액부족출력
                self.cash-=num
                print(place,'에서',num,'원이 사용되었습니다.')
            else:
                print('잔액이 부족합니다.') 
        else:
            if self.cash>=num:
                self.cash-=num
                print(place,'에서',num,'원이 사용되었습니다.')
            else:
                print('잔액이 부족합니다.')

m_card1=Movie_Card()
m_card1.charge(100000)
m_card1.consume(12000,'영화관')
m_card1.consume(30000,'주유소')
m_card1.consume(2000,'편의점')

#%%
#Q.영화관과 주유소에서는 20%할인되게 코드를 수정하시오
#부모클래스
class Card(): 
    def __init__(self):
        self.cash=0
        print('카드가 발급되었습니다.')
    def charge(self,num):
        self.cash += num
        print('%d원이 충전되었습니다.' %(num))
    def consume(self,num):
        if self.cash>=num:   #잔액이 소비하는 돈보다 커야지만 쓸수있게
            self.cash-=num
            print('%d원이 사용되었습니다.' %(num))
        else: 
            print('잔액이 부족합니다.')

#자식클래스
class Movie_Card(Card): #내 클래스이름(무보클래스인 상속받은 클래스이름)
    def consume(self,num,place): #부모클래스의 consume을 내 consume으로 덮어쓰기(overriding)
        if place=='영화관':
            num=0.8*num
            if self.cash>=num: #잔액이 num보다 크다면 카드를 사용하고 아니면 잔액부족출력
                self.cash-=num
                print(place,'에서',num,'원이 사용되었습니다.')
            else:
                print('잔액이 부족합니다.') 
        else:
            if self.cash>=num:
                self.cash-=num
                print(place,'에서',num,'원이 사용되었습니다.')
            else:
                print('잔액이 부족합니다.')

m_card1=Movie_Card()
m_card1.charge(20000)
m_card1.consume(12000,'영화관')
m_card1.consume(30000,'주유소')
m_card1.consume(2000,'편의점')

#%%
#영화관과 주유소에서는 20%할인되게하고 스타벅스에서는 10%할인되게 코드를 수정하시오
#부모클래스
class Card(): 
    def __init__(self):
        self.cash=0
        print('카드가 발급되었습니다.')
    def charge(self,num):
        self.cash += num
        print('%d원이 충전되었습니다.' %(num))
    def consume(self,num):
        if self.cash>=num:   #잔액이 소비하는 돈보다 커야지만 쓸수있게
            self.cash-=num
            print('%d원이 사용되었습니다.' %(num))
        else: 
            print('잔액이 부족합니다.')

#자식클래스
class Movie_Card(Card): #내 클래스이름(무보클래스인 상속받은 클래스이름)
    def consume(self,num,place): #부모클래스의 consume을 내 consume으로 덮어쓰기(overriding)
        if place in ('영화관','주유소'):
            num=0.8*num
            if self.cash>=num: #잔액이 num보다 크다면 카드를 사용하고 아니면 잔액부족출력
                self.cash-=num
                print(place,'에서',num,'원이 사용되었습니다.')
            else:    
                print('잔액이 부족합니다.') 
        elif place=='스타벅스':
            num=0.9*num
            if self.cash>=num: #잔액이 num보다 크다면 카드를 사용하고 아니면 잔액부족출력
                self.cash-=num
                print(place,'에서',num,'원이 사용되었습니다.')
            else:
                print('잔액이 부족합니다.') 
        else:
            if self.cash>=num:
                self.cash-=num
                print(place,'에서',num,'원이 사용되었습니다.')
            else:
                print('잔액이 부족합니다.')

m_card1=Movie_Card()
m_card1.charge(100000)
m_card1.consume(12000,'영화관')
m_card1.consume(30000,'주유소')
m_card1.consume(6000,'스타벅스')
m_card1.consume(2000,'편의점')

#%%
#사원이 입사하면 입사한 사원에 대한 이메일을 자동으로 생성하고 이름을 출력하는 
#함수와 월급을 인상하는 함수를 담는 클래스를 생성하시오
class  Employees:#원래는 뒤에()써야하는데 init메소드에 self말고도 다른 변수가 있기 때문에 생략
    raise_amount = 1.1  # 클래스 변수, 앞에 self. 안붙임
    def __init__(self, first, last, pay): # 객체가 만들어질때 바로 작동되는 함수
        self.first = first   #객체를 생성할때 입력값이 3개가 입력되면서 객체가 만들어집니다.
        self.last  = last
        self.pay   = pay
        self.email = first.lower() + '.' + last.lower() + '@gmail.com'
        self.raise_amount = 1.1  # 인스턴스 변수, 앞에 self. 붙임

    def  full_name(self): #사원의 전체이름을 출력하는 함수
        return '{} {}'.format(self.first, self.last) #중괄호에 각각 first, last가 들어감. respectively
        #return이랑 print랑 똑같은데 return을 쓰면 밑에 출력할떄 꼭 print()로 둘러줘야 결과가 보임
        #print를 처음부터 쓰면 return 안써도되고, 밑에도 print()로 둘러주지 않아도 됨.
    def  apply_raise(self): # 월급을 인상하는 함수
        self.pay = int( self.pay * self.raise_amount)


emp_chulsu = Employees('chulsu', 'kim', 5000000)
print(emp_chulsu.pay)   # 5000000
print(emp_chulsu.email)
emp_chulsu.apply_raise()
print(emp_chulsu.pay)  # 5500000

#%%
#Q.위의 코드에 chulsu2라는 사원이 입사했는데 본인의 월급을 20인상시키는 인스턴스변수를 알아내서
#메소드를 실행했다.
emp_chulsu2 = Employees('chulsu2', 'kim', 5000000)
emp_chulsu2.raise_amount = 1.2
print(emp_chulsu2.pay)   # 5000000
emp_chulsu2.apply_raise()
print(emp_chulsu2.pay)  # 6000000

#%%
#Q.위의 문제에서처럼 임의로 인스턴스변수를 변경하지 못하게 하는 코드를 생성하시오
class  Employees:
    raise_amount = 1.1  # 클래스 변수
    def __init__(self, first, last, pay): # 객체가 만들어질때
        self.first = first               # 바로 작동되는 함수
        self.last  = last
        self.pay   = pay
        self.email = first.lower() + '.' + last.lower() + '@gmail.com'
        self.raise_amount = 1.1  # 인스턴스 변수

    def  full_name(self): #사원의 전체이름을 출력하는 함수
        return  '{} {}'.format(self.first, self.last)

    def  apply_raise(self): # 월급을 인상하는 함수
        self.pay = int( self.pay * Employees.raise_amount)  # 클래스 변수를 사용 


emp_chulsu2 = Employees('chulsu2', 'kim', 5000000)

emp_chulsu2.raise_amount = 1.2   # 인스턴스 변수만 변경할 수 있고 클래스 변수는
                                             # 변경할 수 없다. 

print(emp_chulsu2.pay)   # 5000000
emp_chulsu2.apply_raise()
print(emp_chulsu2.pay)  # 5500000

#%%
#예외처리 이해하기
#try_except를 사용해서 예외처리를 하지 않았을 떄의 코드
def my_divide():
    x=input('분자의 숫자를 입력하세요')
    y=input('분모의 숫자를 입력하세요')
    print (int(x) / int(y))
print(my_divide() )

#%%
#try_except를 사용해서 예외처리 했을 때의 예제
def my_divide():
    try:
        x=input('분자의 숫자를 입력하세요')
        y=input('분모의 숫자를 입력하세요')
        return int(x)/int(y)
    except:
        return '잘못된 값을 입력하셔서 나누기를 할 수 없습니다. '
print(my_divide())

#%%
#Q.판다스를 이용해서 emp3.csv에서 이름, 월급을 출력하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
print(emp[['ename','job']])

#%%
#Q.이름이 SCOTT인 사원의 이름, 월급을 출력하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
print(emp[['ename','job']] [emp['ename']=='SCOTT'])

#%%
#input 함수를 이용해서 이름을 물어보고 그 이름에 해당하는 사원의 이름, 월급을 출력하시오
name=input('이름을 입력하세요')
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
print(emp[['ename','job']] [emp['ename']==name])

#%%
#Q.이번에는 소문자로 이름을 입력해도 출력되게 하시오
name=input('이름을 입력하세요')
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
print(emp[['ename','job']] [emp['ename']==name.upper()])

#%%
#Q. 숫자를 입력하면 해당 숫자의 제곱값이 출력되는 코드를구현하시오
num=int(input('숫자를 입력하세요'))
print(int(num**2))

#%%
#Q.try except를 이용해서 문자를 입력하면 잘못된 값을 입력했다는 메세지가 출력되게하시오
try:
    num1=int(input('숫자를 입력하세요'))
    print(num1**2)
except:
    print('잘못된 값을 입력하셨습니다.')

#%%
#try~except~else 사용하기
try:
    num1=int(input('숫자를 입력하세요'))
    print(num1**2)
except:
    print('잘못된 값을 입력하셨습니다.')
else:
    print('결과 출력에 성공했습니다.')

#%%
#Q.나누기 프로그램을 수정해서 성공하면 성공적으로 나누기를 실행하였습니다. 라는 메세지가 출력되게하시오
def my_divide():
    try:    
        x=input('분자의 숫자를 입력하세요')
        y=input('분모의 숫자를 입력하세요')
        print (int(x) / int(y) )
    except:
        return '잘못된 값을 입력하셔서 나누기를 할 수 없습니다.'
    else:
        return '성공적으로 나누기를 실행하였습니다.'
print(my_divide() )

#%%
#try~except~fianlly 구문 이해하기
try: 
    print('안녕하세요')
except:
    print('예외가 발생했습니다')
finally:
    print('저는 무조건 실행됩니다')

#%%
#Q.나누기 프로그램에서 오류에 상관없이 무조건 이름이 만든 프로그램입니다. 라는 메세지가출력되게하시오
def my_divide():
    try:    
        x=input('분자의 숫자를 입력하세요')
        y=input('분모의 숫자를 입력하세요')
        print (int(x) / int(y) )
    except:
        return '잘못된 값을 입력하셔서 나누기를 할 수 없습니다.'
    finally:
        return '이름이 만든 프로그램입니다.'
print(my_divide() )

#%%
#Q.동전을 10번 던져서 앞면이 2번 나올 확률을 출력하세요
import random
coin=['앞면','뒷면']
cnt=0
for j in range(1,10001):
    a=[]
    for i in range(1,11):
        result=random.choice(coin)
        a.append(result)
    if a.count('앞면')==2:
        cnt+=1
print(cnt)

#%%
#Q.위의 코드를 함수로 생성하여 확률이 출력되게하시오 coin_prob(2) #0.04314
x = int (input('숫자를 입력하세요~')) 
def coin_prob(x): 
    import random 
    coin = ['앞면', '뒷면'] 
    cnt2 = 0 
    for i in range (1, 10001): 
        cnt = 0 
        for j in range (1, 11): 
            if random.choice(coin) == '앞면': 
                cnt = cnt + 1 
        if cnt == x: 
            cnt2 = cnt2 + 1 
    return cnt2/10000 

print (coin_prob(x))  
