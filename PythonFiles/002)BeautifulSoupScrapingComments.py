# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:47:07 2020
@author: jw
"""
#%%
#BeautifulSoup실전1-BeautifulSoup을 이용하여 저장하지 않고 스크래핑하기
#step1. html 불러오기
from bs4 import BeautifulSoup
import urllib.request  #웹 상의 url을 파이썬이 인식할 수 있도록 해주는 모듈입니다.
list_url = "https://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url=urllib.request.Request(list_url) #위의 url을 사람언어->파이썬 언어로 변환, 첫번째 변환
result=urllib.request.urlopen(url).read().decode("utf-8") #위의 url의 html 문서들을 result 변수에 담았다.
print(result) #위의 url의 html 전체 문서가 다 출력되고 있습니다.

#%%
#BeautifulSoup실전1-BeautifulSoup을 이용하여 저장하지 않고 스크래핑하기
#step2. html 파싱하기
from bs4 import BeautifulSoup
import urllib.request
list_url = "https://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url=urllib.request.Request(list_url) 
result=urllib.request.urlopen(url).read().decode("utf-8")
soup=BeautifulSoup(result,"html.parser") #파싱해서 원하는 코드에 빨리 원하는 html에 접근할 수 있게 되었다.
print(soup)

#%%
#BeautifulSoup실전1-BeautifulSoup을 이용하여 저장하지 않고 스크래핑하기
#step3. 웹페이지의 전체에서 시청자 의견 부분만 불러오기
from bs4 import BeautifulSoup
import urllib.request
list_url = "https://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url=urllib.request.Request(list_url) 
result=urllib.request.urlopen(url).read().decode("utf-8")
soup=BeautifulSoup(result,"html.parser") 
result2=soup.find_all('p',class_ ='con') #find만 하면 맨 처음 하나만 가져오고 find_all은 클래스에 해당하는 부분 전부 가져옴.
print(result2)

#%%
#BeautifulSoup실전1-BeautifulSoup을 이용하여 저장하지 않고 스크래핑하기
#step4. 위의 결과에서 html말고 한글부분만 가져오기
from bs4 import BeautifulSoup
import urllib.request
list_url = "https://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url=urllib.request.Request(list_url) 
result=urllib.request.urlopen(url).read().decode("utf-8")
soup=BeautifulSoup(result,"html.parser") 
result2=soup.find_all('p',class_ ='con') #find만 하면 맨 처음 하나만 가져오고 find_all은 클래스에 해당하는 부분 전부 가져옴.
for i in result2:
    print(i.get_text())

#%%
#BeautifulSoup실전1-BeautifulSoup을 이용하여 저장하지 않고 스크래핑하기
#step5. 위의 결과를 깔끔하게 나오게 하기
from bs4 import BeautifulSoup
import urllib.request
list_url = "https://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url=urllib.request.Request(list_url) 
result=urllib.request.urlopen(url).read().decode("utf-8")
soup=BeautifulSoup(result,"html.parser") 
result2=soup.find_all('p',class_ ='con') #find만 하면 맨 처음 하나만 가져오고 find_all은 클래스에 해당하는 부분 전부 가져옴.
for i in result2:
    print(i.get_text(" ", strip=True)) #strip으로 공백 잘라내기

#%%
#BeautifulSoup실전1-BeautifulSoup을 이용하여 저장하지 않고 스크래핑하기
#step6. 위의 결과를 params라는 빈 리스트 안에 넣으시오
from bs4 import BeautifulSoup
import urllib.request
list_url = "https://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url=urllib.request.Request(list_url) 
result=urllib.request.urlopen(url).read().decode("utf-8")
soup=BeautifulSoup(result,"html.parser") 
result2=soup.find_all('p',class_ ='con') 
params=[]
for i in result2:
    params.append(i.get_text(" ", strip=True)) 
print(params)

#%%
#BeautifulSoup실전1-BeautifulSoup을 이용하여 저장하지 않고 스크래핑하기
#step6. 위의 결과를 params라는 빈 리스트 안에 넣으시오
#웹에서 html문서를 가져와 BeautifulSoup으로 파싱
from bs4 import BeautifulSoup
import urllib.request
list_url = "https://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url=urllib.request.Request(list_url) 
result=urllib.request.urlopen(url).read().decode("utf-8")
soup=BeautifulSoup(result,"html.parser")
#댓글 가져오기
result2=soup.find_all('p',class_ ='con') 
params=[]
for i in result2:
    params.append(i.get_text(" ", strip=True)) 
print(params)
#날짜 가져오기
result3=soup.find_all('span',class_ ='date') 
params2=[]
for i in result3:
    params2.append(i.get_text(" ", strip=True)) 
print(params2)

#%%
#BeautifulSoup실전1-BeautifulSoup을 이용하여 저장하지 않고 스크래핑하기
#step6. 날짜와 댓글을 함께 출력하기
#웹에서 html문서를 가져와 BeautifulSoup으로 파싱
from bs4 import BeautifulSoup
import urllib.request
list_url = "https://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url=urllib.request.Request(list_url) 
result=urllib.request.urlopen(url).read().decode("utf-8")
soup=BeautifulSoup(result,"html.parser")
#날짜, 댓글 함께 출력하기
result2=soup.find_all('p',class_ ='con') 
result3=soup.find_all('span',class_ ='date')
params1=[]
params2=[]
for i,j in zip(result3,result2):
    params1.append(i.get_text(" ", strip=True))
    params2.append(j.get_text(" ", strip=True))

for k,h in zip(params1,params2):
    print(k+'    '+h)

#%%
#모든 댓글 페이지의 댓글들 가져오는법(하드코딩하지 않고)
for i in range(1,23):
    print('http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page='+str(i)+'&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&')

#%%
#BeautifulSoup실전1-BeautifulSoup을 이용하여 저장하지 않고 스크래핑하기
#step7. 모든 댓글 페이지의 날짜, 댓글 가져오기
from bs4 import BeautifulSoup
import urllib.request
for i in range(1,23):
    list_url='http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page='+str(i)+'&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&'
    url=urllib.request.Request(list_url) 
    result=urllib.request.urlopen(url).read().decode("utf-8")
    soup=BeautifulSoup(result,"html.parser")
    #날짜, 댓글 함께 출력하기
    result2=soup.find_all('p',class_ ='con') 
    result3=soup.find_all('span',class_ ='date')
    params1=[]
    params2=[]
    for i,j in zip(result3,result2):
        params1.append(i.get_text(" ", strip=True))
        params2.append(j.get_text(" ", strip=True))
    
    for k,h in zip(params1,params2):
        print(k+'    '+h)
        
#%%
#BeautifulSoup실전1-BeautifulSoup을 이용하여 저장하지 않고 스크래핑하기
#step8. params1과 params2가 새로운 url이 돌때마다 바뀌는 것이 아니라 모든 페이지의 댓글과 날짜가 들어가게 하시오
#웹스크롤링에 필요한 모듈을 입포트합니다
from bs4 import BeautifulSoup
import urllib.request
#레이디버그 게시판 게시날짜와 게시글 전체를 다 담은 리스트 2개를 만듭니다.
params1=[]
params2=[]
for i in range(1,23):
    #웹에서 html문서를 가져와 BeautifulSoup으로 파싱
    list_url='http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page='+str(i)+'&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&'
    url=urllib.request.Request(list_url) 
    result=urllib.request.urlopen(url).read().decode("utf-8")
    soup=BeautifulSoup(result,"html.parser")
    #시청자게시판의 날짜와 본문내용을 가져옵니다
    result2=soup.find_all('p',class_ ='con') 
    result3=soup.find_all('span',class_ ='date')
    #시청자 게시판의 날짜와 본문을 params1과 params2 리스트에 담습니다
    for i,j in zip(result3,result2):
        params1.append(i.get_text(" ", strip=True))
        params2.append(j.get_text(" ", strip=True))
#날짜와 본문을 같이 출력합니다.
for k,h in zip(params1,params2):
    print(k+'    '+h)

#%%
#텍스트파일로 저장하는 법
text='abcdefghijklmn'
f=open('d:\\data\\mytext32.txt','w',encoding='UTF8')
f.write(text)
f.close()

#%%
#BeautifulSoup실전1-가져온 텍스트들을 mytext34.txt라는 파일에 저장하시오
#웹스크롤링에 필요한 모듈을 입포트합니다
from bs4 import BeautifulSoup
import urllib.request

#레이디버그 게시판 게시날짜와 게시글 전체를 다 담은 리스트 2개를 만듭니다.
params1=[]
params2=[]
f=open('d:\\data\\mytext34.txt','w',encoding='UTF8') #텍스트파일로 저장

for i in range(1,23):
    #웹에서 html문서를 가져와 BeautifulSoup으로 파싱
    list_url='http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page='+str(i)+'&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&'
    url=urllib.request.Request(list_url) 
    result=urllib.request.urlopen(url).read().decode("utf-8")
    soup=BeautifulSoup(result,"html.parser")
    #시청자게시판의 날짜와 본문내용을 가져옵니다
    result2=soup.find_all('p',class_ ='con') 
    result3=soup.find_all('span',class_ ='date')
    #시청자 게시판의 날짜와 본문을 params1과 params2 리스트에 담습니다
    for i,j in zip(result3,result2):
        params1.append(i.get_text(" ", strip=True))
        params2.append(j.get_text(" ", strip=True))
#날짜와 본문을 같이 출력합니다.
for k,h in zip(params1,params2):
    f.write(k+'    '+h+'\n') #mytext34.txt에 입력하기,'\n'은 엔터 라는 뜻으로 한줄씩 엔터치고 쓰

f.close() #mytext34.txt파일 닫기
