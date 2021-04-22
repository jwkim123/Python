# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 09:42:27 2020
@author: jw
"""
#%%
#Q.try~except 구문을 이용하여 나누기 프로그램을 만드시오
try:
    x=int(input('분자의 숫자를 입력하시오'))
    y=int(input('분모의 숫자를 입력하시오'))
    print(x/y)
except ZeroDivisionError: #분모에 0을 입력했을 때 수행
    print('0으로 나눌 수 없습니다.') 
except: #except하고 아무것도 안쓰면 zerodivisionerror말고 다른 모든 에러는 여기서 수행
    print('잘못된 값을 입력하셨습니다.')
    
#%%
#Q.숫자를 물어보게하고 숫자를 입력하면 해당 숫자만큼 1부터 숫자가 출력되는 코드를 작성하시오
num=int(input('숫자를 입력하세요'))
for i in range(1,num+1):
    print(i)
    
#%%
#Q.위의 코드에 예외처리를 해서 문자를 입력하면 잘못된 값을 입력하셨습니다. 라고 메세지가 출력되게하시오
try:
    num=int(input('숫자를 입력하세요'))
    for i in range(1,num+1):
        print(i)
except:
    print('잘못된 값을 입력하셨습니다.')
    
#%%
#Q.에러가 난 이유가 함께 나오도록 코드를 작성하시오
try:
    num=int(input('숫자를 입력하세요'))
    for i in range(1,num+1):
        print(i)
except Exception as e:
    print('잘못된 값을 입력하셨습니다.')
    print(e)
    
#%%
#Q.판다스를 이용해서 데이터를 로드하고 이름을 물어보고 해당 값을 소문자로 입력해도 해당 사원의 월급이 출력되게하시오
#불필요한 결과들 안나오고 월급만 출력되게하시오
name=input('이름을 입력하세요')
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
result=emp['sal'] [emp['ename']==name.upper()].values[0]
print(result)

#%%
#Q.판다스를 이용해서 사원의 이름을 입력받고 월급이 3000이상인 사원들의 월급은 볼 수 없다는 메시지가 나오게 하시오
name=input('이름을 입력하세요')
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
result=emp['sal'] [emp['ename']==name.upper()].values[0] #조건을 sal에 1개만 주니까 출력할 컬럼에 sal만 작성
if result>=3000:
    raise Exception('해당 사원의 월급은 볼 수 없습니다.') #해당하면 에러나면서 밑의 코드들 실행하지않고 끝내버림
print(emp[['ename','sal']] [emp['ename']==name.upper()]) #출력은 ename, sal 둘 다 출력

#%%
#Q.없는 사원의 이름을 입력하면 해당 사원은 없습니다 라는 메세지가 출력되게하시오
try:
    name=input('이름을 입력하세요')
    import pandas as pd
    emp=pd.read_csv("d:\\data\\emp3.csv")
    result=emp['ename'][emp['ename']==name.upper()].values[0] #values[0]을 사용하면 컬럼이 아니라 값으로 출력이 되어서 result에 담기게 됨
    print(emp[['ename','sal']] [emp['ename']==result]) #없는 사원이름을 입력하면 result에 담기지 않아서 검색이 안되어 LookupError예외처리가 됩니다.
except LookupError:
    print('해당 사원은 없습니다.')
    
#%%
#Q.직업을 물어보고 해당 사원의 이름,직업,월급을 출력하는데 없는 직업을 입력하면 해당 직업은 사원테이블에 없습니다.
#라는 메세지가 출력되게 하시오
try:
    job=input('직업을 입력하세요')
    import pandas as pd
    emp=pd.read_csv("d:\\data\\emp3.csv")
    result=emp['job'][emp['job']==job.upper()].values[0] #values[0]을 사용하면 컬럼이 아니라 값으로 출력이 되어서 result에 담기게 됨
    print(emp[['ename','job','sal']] [emp['job']==result]) #없는 사원이름을 입력하면 result에 담기지 않아서 검색이 안되어 LookupError예외처리가 됩니다.
except LookupError:
    print('해당 직업은 사원 테이블에 없습니다.')
    
#%%
#자료형 이해하기
numdata=57
print(type(numdata)) #<class 'int'>

numdata2=57.2
print(type(numdata2)) #<class 'float'>

a=[1,2,3,4]
print(type(a)) #<class 'list'>

a = {'apple':'사과', 'banana':'바나나', 'peach':'복숭아', 'pear':'배'}
print(type(a)) #<class 'dict'>

#%%
#Q.두개의 숫자를 각각 물어보게하고 아래의 메세지가 출력되게 하시오
num1=int(input('첫번째 숫자를 입력하세요'))
num2=int(input('두번째 숫자를 입력하세요'))
result=num1%num2
print('{}을 {}으로 나누면 {}가 나머지로 남습니다.'.format(num1,num2,result))

#%%
#Q.위의 나누기를 다시 하는데 몫과 나머지를 함께 출력되게 하시오. 0을 입력하면 0으로는 나눌 수 없다고 출력되게하시오
try:
    num1=int(input('첫번째 숫자를 입력하세요'))
    num2=int(input('두번째 숫자를 입력하세요'))
    result1,result2=divmod(num1,num2)
    print('{}을 {}으로 나눈 몫은 {}이고 나머지는 {}입니다.'.format(num1,num2,result1,result2))
except ZeroDivisionError: #분모에 0을 입력했을 때 수행
    print('0으로 나눌 수 없습니다.') 

#%%
#Q.dept3 테이블을 판다스로 로드하시오
import pandas as pd
dept=pd.read_csv("d:\\data\\dept3.csv")
print(dept)

#%%
#Q.부서위치가 DALLAS의 부서번호와 부서명을 출력하시오
import pandas as pd
dept=pd.read_csv("d:\\data\\dept3.csv")
print(dept[['deptno','dname']][dept['loc']=='DALLAS'])

#%%
#emp3.csv와 dept3.csv 조인하여 이름, 부서위치를 출력하기
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
dept=pd.read_csv("d:\\data\\dept3.csv")
result=pd.merge(emp, dept, on='deptno' )
print(result)
print(result[['ename', 'loc' ]])

#%%
#Q.DALLAS에서 근무하는 사원들의 이름과 부서위치를 출력하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
dept=pd.read_csv("d:\\data\\dept3.csv")
result=pd.merge(emp,dept,on='deptno')
print(result[['ename', 'loc' ]] [result['loc']=='DALLAS'])

#%%
#Q.월급이 3000이상인 사원들의 이름, 월급, 부서위치를 출력하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
dept=pd.read_csv("d:\\data\\dept3.csv")
result=pd.merge(emp,dept,on='deptno')
print(result[['ename','sal','loc']] [result['sal']==3000])

#%%
#Q.부서번호가 10번, 20번인 사원들의 이름, 부서위치, 부서번호를 출력하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
dept=pd.read_csv("d:\\data\\dept3.csv")
result=pd.merge(emp,dept,on='deptno')
print(result[['ename','loc','deptno']] [result['deptno'].isin([10,20])])

#%%
#Q.월급이 1000애서 3000사이인 사원들의 이름, 월급, 부서위치를 출력하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
dept=pd.read_csv("d:\\data\\dept3.csv")
result=pd.merge(emp,dept,on='deptno')
print(result[['ename','sal','loc']] [result['sal'].between(1000,3000) ])

#%%
#위의 결과를 월급이 높은순부터 낮은순으로 정렬하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
dept=pd.read_csv("d:\\data\\dept3.csv")
result=pd.merge(emp,dept,on='deptno')
result1=result[['ename','sal','loc']] [result['sal'].between(1000,3000) ]
print(result1.sort_values('sal',ascending=False))

#%%
#Q.아래의 SQL을 Pandas로 구현하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
dept=pd.read_csv("d:\\data\\dept3.csv")
result=pd.merge(emp,dept,how='right')
print(result[['ename','loc']])

#%%
#아래의 SQL을 Pandas로 구현하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
dept=pd.read_csv("d:\\data\\dept3.csv")
result=pd.merge(emp,dept,how='outer')
print(result[['ename','loc']])

#%%
#다음의 SQL을 Pandas로 구현하시오
#select ename, sal from emp where sal>(select sal from emp where ename='JONES')
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
dept=pd.read_csv("d:\\data\\dept3.csv")
jsal=emp['sal'][emp['ename']=='JONES'].values[0] #values를 붙여줘야 컬럼이 아닌 하나의 값이 jsal에 담긴다
print(emp[['ename','sal']] [emp['sal']>jsal])

#%%
#Q.아래의 서브쿼리를 Pandas로 구현하시오
#select ename, sal, from emp where job=(select job from emp where ename='SCOTT');
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
dept=pd.read_csv("d:\\data\\dept3.csv")
jsal=emp['job'][emp['ename']=='SCOTT'].values[0] 
print(emp[['ename','sal']] [emp['job']==jsal])

#%%
#Q.아래의 서브쿼리를 Pandas로 구현하시오
#select ename, sal, from emp where job=(select job from emp where ename='SCOTT') and ename!='SCOTT';
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
dept=pd.read_csv("d:\\data\\dept3.csv")
jsal=emp['job'][emp['ename']=='SCOTT'].values[0] 
print(emp[['ename','sal']] [(emp['job']==jsal) & (emp['ename']=='SCOTT')])

#%%
#아래의 SQL을 판다스로 구현하시오
#select max(sal) from emp where deptno=20;
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
print(emp['sal'] [emp['deptno']==20].max())

#%%
#아래의 SQL을 판다스로 구현하시오
#select min(sal) from emp where job='SALESMAN';
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
print(emp['sal'] [emp['job']=='SALESMAN'].min())

#%%
#Q.emp12.csv를 판다스 데이터 프레임으로 만들어서 출력하고 우리반에서 최소 나이를 출력하시오
import pandas as pd
emp12=pd.read_csv("d:\\data\\emp12.csv")
print(emp12['AGE'].min())

#%%
#Q.아래의 SQL을 판다스로 구현하시오
#select max(sal) from emp group by job;
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
result=emp.groupby('job')['sal'].max().reset_index()
print(result)

#%%
#Q.다음의 SQL을 판다스로 구현하시오
#select deptno, sum(sal) from emp group by deptno;
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
result=emp.groupby('deptno')['sal'].sum().reset_index()
print(result)

#%%
#Q.다음의 SQL을 판다스로 구현하시오
#select deptno, sum(sal) from emp where deptno!=20 group by deptno;
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
result=emp.groupby('deptno')['sal'].sum().reset_index()
print(result[['deptno','sal']][result['deptno']!=20])

#%%
#Q.동전을 10번 던져서 0~10개의 앞면이 나올 확률을 한번에 출력하시오
def coin_prob(num):
    import random
    coin=['앞면','뒷면']
    cnt=0
    for k in range(1,10001):
        a=[]
        for i in range(1,11):
            a.append(random.choice(coin))
        if a.count('앞면')==num:
            cnt+=1
    return cnt/10000

for i in range(0,11):		        
    print("동전을 10번 던져서 {}개 앞면이 나올 확률 {}" .format(i,coin_prob(i)))
