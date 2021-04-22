# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 09:37:33 2020
@author: jw
Connect Python with MySQL
"""
import cx_Oracle
import pandas as pd

dsn=cx_Oracle.makedsn("localhost",1521,'orcl') #오라클 주소
db=cx_Oracle.connect('scott','tiger',dsn) #오라클 접속 유저 정보
cursor=db.cursor() #결과 데이터를 담을 메모리 이름을 cursor로 선언
cursor.execute("""select * from emp""") #작성한 쿼리문의 결과가 커서 메모리에 담김
row=cursor.fetchall() #cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다
emp=pd.DataFrame(row)
print(emp)

#%%
#Q.select empno, ename, sal, deptno from emp를 수행하시오
import cx_Oracle
import pandas as pd

dsn=cx_Oracle.makedsn("localhost",1521,'orcl') #오라클 주소
db=cx_Oracle.connect('scott','tiger',dsn) #오라클 접속 유저 정보
cursor=db.cursor() #결과 데이터를 담을 메모리 이름을 cursor로 선언
cursor.execute("""select empno,ename,sal,deptno from emp""") #작성한 쿼리문의 결과가 커서 메모리에 담김
row=cursor.fetchall() #cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다
emp=pd.DataFrame(row)
print(emp)

#%%
#Q.dept 테이블의 모든 데이터를 조회하시오
import cx_Oracle
import pandas as pd

dsn=cx_Oracle.makedsn("localhost",1521,'orcl') #오라클 주소
db=cx_Oracle.connect('scott','tiger',dsn) #오라클 접속 유저 정보
cursor=db.cursor() #결과 데이터를 담을 메모리 이름을 cursor로 선언
cursor.execute("""select * from dept""") #작성한 쿼리문의 결과가 커서 메모리에 담김
row=cursor.fetchall() #cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다
dept=pd.DataFrame(row)
print(dept)

#%%
#Q.월급이 1200 이상인 사원들의 이름, 월급을 출력하시오
import cx_Oracle
import pandas as pd

dsn=cx_Oracle.makedsn("localhost",1521,'orcl') #오라클 주소
db=cx_Oracle.connect('scott','tiger',dsn) #오라클 접속 유저 정보
cursor=db.cursor() #결과 데이터를 담을 메모리 이름을 cursor로 선언
cursor.execute("""select ename,sal from emp where sal>=1200""") #작성한 쿼리문의 결과가 커서 메모리에 담김
row=cursor.fetchall() #cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다
emp=pd.DataFrame(row)
print(emp)

#%%
#Q.emp 테이블의 월급을 막대 그래프로 그리시오
import cx_Oracle
import pandas as pd

dsn=cx_Oracle.makedsn("localhost",1521,'orcl') #오라클 주소
db=cx_Oracle.connect('scott','tiger',dsn) #오라클 접속 유저 정보
cursor=db.cursor() #결과 데이터를 담을 메모리 이름을 cursor로 선언
cursor.execute("""select ename,sal from emp""") #작성한 쿼리문의 결과가 커서 메모리에 담김
row=cursor.fetchall() #cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다
emp=pd.DataFrame(row)
emp.index=list(emp[0])
emp.plot(kind='bar')

#%%
#Q.위의 그래프의 색을 변경하시오
import cx_Oracle
import pandas as pd

dsn=cx_Oracle.makedsn("localhost",1521,'orcl') #오라클 주소
db=cx_Oracle.connect('scott','tiger',dsn) #오라클 접속 유저 정보
cursor=db.cursor() #결과 데이터를 담을 메모리 이름을 cursor로 선언
cursor.execute("""select ename,sal from emp""") #작성한 쿼리문의 결과가 커서 메모리에 담김
row=cursor.fetchall() #cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다
emp=pd.DataFrame(row)
emp.index=list(emp[0])
emp.plot(kind='bar',color='magenta')

#%%
#Q.직업, 직업별 최대월급을 출력하시오
import cx_Oracle
import pandas as pd

dsn=cx_Oracle.makedsn("localhost",1521,'orcl') #오라클 주소
db=cx_Oracle.connect('scott','tiger',dsn) #오라클 접속 유저 정보
cursor=db.cursor() #결과 데이터를 담을 메모리 이름을 cursor로 선언
cursor.execute("""select job, max(sal) from emp group by job""") #작성한 쿼리문의 결과가 커서 메모리에 담김
row=cursor.fetchall() #cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다
emp=pd.DataFrame(row)
print(emp)

#%%
#Q.직업 직업별 토탈월급을 출력하는데 토탈월급이 높은 것부터 출력하시오
import cx_Oracle
import pandas as pd

dsn=cx_Oracle.makedsn("localhost",1521,'orcl') #오라클 주소
db=cx_Oracle.connect('scott','tiger',dsn) #오라클 접속 유저 정보
cursor=db.cursor() #결과 데이터를 담을 메모리 이름을 cursor로 선언
cursor.execute("""select job, sum(sal) 
                   from emp 
                   group by job 
                   order by 2 desc""") #작성한 쿼리문의 결과가 커서 메모리에 담김
row=cursor.fetchall() #cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다
emp=pd.DataFrame(row)
print(emp)

#%%
#Q.이름, 월급, 순위를 출력하는데 순위가 월급이 높은 사원순으로 출력하시오
import cx_Oracle
import pandas as pd

dsn=cx_Oracle.makedsn("localhost",1521,'orcl') #오라클 주소
db=cx_Oracle.connect('scott','tiger',dsn) #오라클 접속 유저 정보
cursor=db.cursor() #결과 데이터를 담을 메모리 이름을 cursor로 선언
cursor.execute("""select ename, sal, dense_rank() over (order by sal desc) 
                   from emp """) #작성한 쿼리문의 결과가 커서 메모리에 담김
row=cursor.fetchall() #cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다
emp=pd.DataFrame(row)
print(emp)

#%%
#Q.부서번호, 부서번호별 토탈월급을 출력하시오
import cx_Oracle
import pandas as pd

dsn=cx_Oracle.makedsn("localhost",1521,'orcl') #오라클 주소
db=cx_Oracle.connect('scott','tiger',dsn) #오라클 접속 유저 정보
cursor=db.cursor() #결과 데이터를 담을 메모리 이름을 cursor로 선언
cursor.execute("""select deptno, sum(sal) 
                   from emp
                   group by deptno""") #작성한 쿼리문의 결과가 커서 메모리에 담김
row=cursor.fetchall() #cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다
emp=pd.DataFrame(row)
print(emp)

#%%
#Q.위의 결과를 막대그래프로 시각화하시오
import cx_Oracle
import pandas as pd

dsn=cx_Oracle.makedsn("localhost",1521,'orcl') #오라클 주소
db=cx_Oracle.connect('scott','tiger',dsn) #오라클 접속 유저 정보
cursor=db.cursor() #결과 데이터를 담을 메모리 이름을 cursor로 선언
cursor.execute("""select deptno, sum(sal) 
                   from emp
                   group by deptno""") #작성한 쿼리문의 결과가 커서 메모리에 담김
row=cursor.fetchall() #cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다
emp=pd.DataFrame(row)
emp.index=list(emp[0])
emp.plot(kind='bar',color='magenta')

#%%
#Q.emp테이블 전체를 출력하는데 컬럼명도 함께 출력되게하시오
import cx_Oracle
import pandas as pd

dsn=cx_Oracle.makedsn("localhost",1521,'orcl') #오라클 주소
db=cx_Oracle.connect('scott','tiger',dsn) #오라클 접속 유저 정보
cursor=db.cursor() #결과 데이터를 담을 메모리 이름을 cursor로 선언
cursor.execute("""select * 
                   from emp""") #작성한 쿼리문의 결과가 커서 메모리에 담김
row=cursor.fetchall() #cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다
colname=cursor.description #컬럼명을 가져온다
col=[]
for i in colname: #컬럼명을 리스트에 담는다
    col.append(i[0].lower())

emp=pd.DataFrame(list(row), columns=col)
print(emp)

#%%
#Q.이름, 월급을 출력하는데 월급이 3000이상으로 조건을 주시오(판다스 이용)
import cx_Oracle
import pandas as pd

dsn=cx_Oracle.makedsn("localhost",1521,'orcl') #오라클 주소
db=cx_Oracle.connect('scott','tiger',dsn) #오라클 접속 유저 정보
cursor=db.cursor() #결과 데이터를 담을 메모리 이름을 cursor로 선언
cursor.execute("""select * 
                   from emp""") #작성한 쿼리문의 결과가 커서 메모리에 담김
row=cursor.fetchall() #cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다
colname=cursor.description #컬럼명을 가져온다
col=[]
for i in colname: #컬럼명을 리스트에 담는다
    col.append(i[0].lower())

emp=pd.DataFrame(list(row), columns=col)
print(emp[['ename','sal']][emp['sal']>=3000])

#%%
#Q.이름과 부서위치를 출력하시오
import cx_Oracle
import pandas as pd

dsn=cx_Oracle.makedsn("localhost",1521,'orcl') #오라클 주소
db=cx_Oracle.connect('scott','tiger',dsn) #오라클 접속 유저 정보
cursor=db.cursor() #결과 데이터를 담을 메모리 이름을 cursor로 선언
cursor.execute("""select e.ename, d.loc
                   from emp e, dept d
                   where e.deptno = d.deptno""") #작성한 쿼리문의 결과가 커서 메모리에 담김
row=cursor.fetchall() #cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다
colname=cursor.description #컬럼명을 가져온다
col=[]
for i in colname: #컬럼명을 리스트에 담는다
    col.append(i[0].lower())

emp=pd.DataFrame(list(row), columns=col)
print(emp)

#%%
#Q.부서위치, 부서위치별 토탈월급을 출력하고 막대그래프로 나타내시오
import cx_Oracle
import pandas as pd

dsn=cx_Oracle.makedsn("localhost",1521,'orcl') #오라클 주소
db=cx_Oracle.connect('scott','tiger',dsn) #오라클 접속 유저 정보
cursor=db.cursor() #결과 데이터를 담을 메모리 이름을 cursor로 선언
cursor.execute("""select d.loc, sum(e.sal)
                   from emp e, dept d
                   where e.deptno = d.deptno
                   group by d.loc""") #작성한 쿼리문의 결과가 커서 메모리에 담김
row=cursor.fetchall() #cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다
colname=cursor.description #컬럼명을 가져온다
emp=pd.DataFrame(row)
emp.index=list(emp[0])
emp.plot(kind='bar',color='magenta')

#%%
#Q.MySQL과 파이썬을 연동해서 EMP테이블을 파이썬에서 출력하시오
import pymysql,pandas as pd

conn = pymysql.connect(host="localhost", user="root",password="oracle", db="orcl",charset="utf8")

curs = conn.cursor()
sql = "select * from emp"
curs.execute(sql)
rows = curs.fetchall()
colname = curs.description
col = []
for i in colname:
    col.append(i[0].upper())
emp = pd.DataFrame(list(rows),columns=col)
print(emp[['ENAME', 'SAL']] )

#%%
#Q.직업, 직업별 토탈월급을 출력하시오
import pymysql,pandas as pd 

conn = pymysql.connect(host="localhost", user="root",password="oracle", db="orcl",charset="utf8")

curs = conn.cursor()
sql = "select job, sum(sal) from emp group by job"
curs.execute(sql)
rows = curs.fetchall()
emp = pd.DataFrame(list(rows),columns=col)
print(emp)

#%%
#Q.위의 결과를 막대그래프로 시각화하시오
import pymysql
import pandas as pd

conn = pymysql.connect(host="localhost", user="root",password="oracle",
                       db="orcl",charset="utf8")

curs = conn.cursor()
sql = """ select job, sum(sal) from emp group by job """
             
curs.execute(sql)
row = curs.fetchall()  
emp = pd.DataFrame(row)
print(emp)

for i in emp.columns:
    try: 
        emp[i]=emp[i].astype(int)
    except:
        pass
emp.index = list(emp[0])
emp.plot( kind='bar', color='red')

#%%
#Q.오라클과 파이썬을 연동하여 아래의 사원들을 검색하시오. 이름, 월급, 부서번호, 자기가 속한 부서번호의 평균월급을 출력하는데
#자신의 월급이 자기가 속한 부서번호의 평균월급보다 더 큰 사원들만 출력하시오
import cx_Oracle
import pandas as pd

dsn=cx_Oracle.makedsn("localhost",1521,'orcl') #오라클 주소
db=cx_Oracle.connect('scott','tiger',dsn) #오라클 접속 유저 정보
cursor=db.cursor() #결과 데이터를 담을 메모리 이름을 cursor로 선언
cursor.execute("""select e.ename, e.sal, e.deptno, v.평균
                   from emp e, (select deptno, avg(sal) 평균
                                from emp
                                group by deptno) v
                   where e.deptno=v.deptno and e.sal>v.평균""") #작성한 쿼리문의 결과가 커서 메모리에 담김
row=cursor.fetchall() #cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다
emp=pd.DataFrame(row)
print(emp)
