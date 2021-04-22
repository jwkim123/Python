# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 15:56:10 2020
@author: jw
"""
#%%
#BeautifulSoup실전3-1.동아일보에서 인공지능을 검색하고 기사들의 리스트가 있는 페이지의 url을 가져오기
from bs4 import BeautifulSoup
import urllib.request
#중앙일보에서 인공지능으로 검색했을 때 나오는 첫페이지의 html코드를 BeautifulSoup에서 이용할 수 있도록 파싱
list_url = "https://www.donga.com/news/search?p=1&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1"
url=urllib.request.Request(list_url) 
result=urllib.request.urlopen(url).read().decode("utf-8")
soup=BeautifulSoup(result,"html.parser") #파싱해서 원하는 코드에 빨리 원하는 html에 접근할 수 있게 되었다.
print(soup)

#%%
#BeautifulSoup실전3-1.동아일보에서 인공지능 검색
#웹스크롤링에 필요한 모듈 임포트
from bs4 import BeautifulSoup
import urllib.request
#중앙일보에서 인공지능으로 검색했을 때 나오는 첫페이지의 html코드를 BeautifulSoup에서 이용할 수 있도록 파싱
def d_scroll():
    list_url = 'https://www.donga.com/news/search?p=1&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1'
    url=urllib.request.Request(list_url) 
    result=urllib.request.urlopen(url).read().decode("utf-8")
    soup=BeautifulSoup(result,"html.parser") #파싱해서 원하는 코드에 빨리 원하는 html에 접근할 수 있게 되었다.
    result1=soup.find_all('p',class_ ='txt')
    params=[]
    for i in result1: #result1의 요소를 하나씩 빼낸다.
        for k in i: #h2태그 안의 a태그의 html코드를 가져오기 위한 코드
            params.append(k.get('href')) #a태그의 href의 값을 얻어내라
    return params

print(d_scroll())

#%%
#BeautifulSoup실전3-2.동아일보에서 인공지능 검색 
#웹스크롤링에 필요한 모듈 임포트
from bs4 import BeautifulSoup
import urllib.request
    #중앙일보에서 상세기사 url로 검색했을 때 나오는 첫페이지의 html코드를 BeautifulSoup에서 이용할 수 있도록 파싱
def d_detail_scroll():
    list_url = "https://www.donga.com/news/article/all/20201211/104398405/2"
    url=urllib.request.Request(list_url) 
    result=urllib.request.urlopen(url).read().decode("utf-8")
    soup=BeautifulSoup(result,"html.parser") #파싱해서 원하는 코드에 빨리 원하는 html에 접근할 수 있게 되었다.
    #상세기사의 본문을 가져올 수 있도록 태그와 클래스를 찾는다. 태그div, 클래스 article_body mg fs4
    result1=soup.find_all('div',class_ ='article_txt')
    #위의 result1은 리스트이므로 forloop문을 이용해서 리스트에 있는 요소를 하나씩 빼내면서 본문의 텍스트를 얻어냅니다.
    params2=[]
    for i in result1: #result1의 요소를 하나씩 빼낸다.
        params2.append(i.get_text(" ",strip=True)) #a태그의 href의 값을 얻어내라
    return params2

print(d_detail_scroll())


#%%
#BeautifulSoup실전3-2.동아일보에서 인공지능 검색 
#웹스크롤링에 필요한 모듈 임포트
from bs4 import BeautifulSoup
import urllib.request
#중앙일보에서 인공지능으로 검색했을 때 나오는 첫페이지의 html코드를 BeautifulSoup에서 이용할 수 있도록 파싱
def d_scroll():
    list_url = 'https://www.donga.com/news/search?p=1&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1'
    url=urllib.request.Request(list_url) 
    result=urllib.request.urlopen(url).read().decode("utf-8")
    soup=BeautifulSoup(result,"html.parser") #파싱해서 원하는 코드에 빨리 원하는 html에 접근할 수 있게 되었다.
    result1=soup.find_all('p',class_ ='txt')
    params=[]
    for i in result1: #result1의 요소를 하나씩 빼낸다.
        for k in i: #h2태그 안의 a태그의 html코드를 가져오기 위한 코드
            params.append(k.get('href')) #a태그의 href의 값을 얻어내라
    return params

#기사들의 본문들을 가져오는 함수
def d_detail_scroll():
    list_url = d_scroll() #특정기사의 url을 쓰면 해당기사의 본문을 가져오지만 j_scroll()함수를 쓰면 함수안의 모든 기사의 url의 본문을 불러옴
    params2=[]
    for i in list_url: #list_url의 모든 url들을 읽어온다
        url=urllib.request.Request(i) 
        result=urllib.request.urlopen(url).read().decode("utf-8")
        soup=BeautifulSoup(result,"html.parser") 
        result1=soup.find_all('div',class_ ='article_txt')
        for i in result1:
            params2.append(i.get_text(" ",strip=True))
    return params2

print(d_detail_scroll())

#%%
#BeautifulSoup실전3-2.한겨레에서 인공지능 검색 
#웹스크롤링에 필요한 모듈 임포트
from bs4 import BeautifulSoup
import urllib.request
#중앙일보에서 인공지능으로 검색했을 때 나오는 첫페이지의 html코드를 BeautifulSoup에서 이용할 수 있도록 파싱
def h_scroll():
    list_url = 'http://search.hani.co.kr/Search?command=query&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&media=news&submedia=&sort=d&period=all&datefrom=1988.01.01&dateto=2020.12.16&pageseq=0'
    url=urllib.request.Request(list_url) 
    result=urllib.request.urlopen(url).read().decode("utf-8")
    soup=BeautifulSoup(result,"html.parser") #파싱해서 원하는 코드에 빨리 원하는 html에 접근할 수 있게 되었다.
    result1=soup.find_all('dt')
    params=[]
    for i in result1: #result1의 요소를 하나씩 빼낸다.
        for k in i: #h2태그 안의 a태그의 html코드를 가져오기 위한 코드
            params.append('http:'+k.get('href')) #a태그의 href의 값을 얻어내라
    return params

print(h_scroll())

#%%
#BeautifulSoup실전3-2.한겨레에서 인공지능 검색 
#웹스크롤링에 필요한 모듈 임포트
from bs4 import BeautifulSoup
import urllib.request
    #중앙일보에서 상세기사 url로 검색했을 때 나오는 첫페이지의 html코드를 BeautifulSoup에서 이용할 수 있도록 파싱
def h_detail_scroll():
    list_url = "http://www.hani.co.kr/arti/opinion/column/974362.html"
    url=urllib.request.Request(list_url) 
    result=urllib.request.urlopen(url).read().decode("utf-8")
    soup=BeautifulSoup(result,"html.parser") #파싱해서 원하는 코드에 빨리 원하는 html에 접근할 수 있게 되었다.
    #상세기사의 본문을 가져올 수 있도록 태그와 클래스를 찾는다. 태그div, 클래스 article_body mg fs4
    result1=soup.find_all('div',class_ ='text')
    #위의 result1은 리스트이므로 forloop문을 이용해서 리스트에 있는 요소를 하나씩 빼내면서 본문의 텍스트를 얻어냅니다.
    params2=[]
    for i in result1: #result1의 요소를 하나씩 빼낸다.
        params2.append(i.get_text(" ",strip=True)) #a태그의 href의 값을 얻어내라
    return params2

print(h_detail_scroll())

#%%
#BeautifulSoup실전3-2.한겨레에서 인공지능 검색 
#웹스크롤링에 필요한 모듈 임포트
from bs4 import BeautifulSoup
import urllib.request
#중앙일보에서 인공지능으로 검색했을 때 나오는 첫페이지의 html코드를 BeautifulSoup에서 이용할 수 있도록 파싱
def h_scroll():
    list_url = 'http://search.hani.co.kr/Search?command=query&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&media=news&submedia=&sort=d&period=all&datefrom=1988.01.01&dateto=2020.12.16&pageseq=0'
    url=urllib.request.Request(list_url) 
    result=urllib.request.urlopen(url).read().decode("utf-8")
    soup=BeautifulSoup(result,"html.parser") #파싱해서 원하는 코드에 빨리 원하는 html에 접근할 수 있게 되었다.
    result1=soup.find_all('dt')
    params=[]
    for i in result1: #result1의 요소를 하나씩 빼낸다.
        for k in i: #h2태그 안의 a태그의 html코드를 가져오기 위한 코드
            params.append('http:'+k.get('href')) #a태그의 href의 값을 얻어내라
    return params

#기사들의 본문들을 가져오는 함수
def h_detail_scroll():
    list_url = h_scroll() #특정기사의 url을 쓰면 해당기사의 본문을 가져오지만 j_scroll()함수를 쓰면 함수안의 모든 기사의 url의 본문을 불러옴
    params2=[]
    for i in list_url: #list_url의 모든 url들을 읽어온다
        url=urllib.request.Request(i) 
        result=urllib.request.urlopen(url).read().decode("utf-8")
        soup=BeautifulSoup(result,"html.parser") 
        result1=soup.find_all('div',class_ ='text')
        for i in result1:
            params2.append(i.get_text(" ",strip=True))
    return params2

print(h_detail_scroll())


#%%
#BeautifulSoup실전3-2.전자신문에서 인공지능 검색 
#웹스크롤링에 필요한 모듈 임포트
from bs4 import BeautifulSoup
import urllib.request
#중앙일보에서 인공지능으로 검색했을 때 나오는 첫페이지의 html코드를 BeautifulSoup에서 이용할 수 있도록 파싱
def jj_scroll():
    list_url = 'https://search.etnews.com/etnews/search.php?category=CATEGORY1&kwd=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&pageNum=1&pageSize=10&reSrchFlag=false&sort=1&startDate=&endDate=&sitegubun=&jisikgubun=&preKwd%5B0%5D=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5'
    url=urllib.request.Request(list_url) 
    result=urllib.request.urlopen(url).read().decode("utf-8")
    soup=BeautifulSoup(result,"html.parser") #파싱해서 원하는 코드에 빨리 원하는 html에 접근할 수 있게 되었다.
    result1=soup.find_all('dt')
    params=[]
    for i in result1: #result1의 요소를 하나씩 빼낸다.
        for k in i: #h2태그 안의 a태그의 html코드를 가져오기 위한 코드
            params.append('http:'+k.get('href')) #a태그의 href의 값을 얻어내라
    return params
print(jj_scroll())

#%%
#BeautifulSoup실전3-2.전자신문에서 인공지능 검색 
#웹스크롤링에 필요한 모듈 임포트
from bs4 import BeautifulSoup
import urllib.request
    #중앙일보에서 상세기사 url로 검색했을 때 나오는 첫페이지의 html코드를 BeautifulSoup에서 이용할 수 있도록 파싱
def jj_detail_scroll():
    list_url = "https://www.etnews.com/20201216000253"
    url=urllib.request.Request(list_url) 
    result=urllib.request.urlopen(url).read().decode("utf-8")
    soup=BeautifulSoup(result,"html.parser") #파싱해서 원하는 코드에 빨리 원하는 html에 접근할 수 있게 되었다.
    #상세기사의 본문을 가져올 수 있도록 태그와 클래스를 찾는다. 태그div, 클래스 article_body mg fs4
    result1=soup.find_all(class_ ='article_body')
    #위의 result1은 리스트이므로 forloop문을 이용해서 리스트에 있는 요소를 하나씩 빼내면서 본문의 텍스트를 얻어냅니다.
    params2=[]
    for i in result1: #result1의 요소를 하나씩 빼낸다.
        params2.append(i.get_text(" ",strip=True)) #a태그의 href의 값을 얻어내라
    return params2

print(jj_detail_scroll())

#%%
#BeautifulSoup실전3-2.전자신문에서 인공지능 검색 

#https://search.etnews.com/etnews/search.php?category=CATEGORY1&kwd=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&pageNum=1&pageSize=10&reSrchFlag=false&sort=1&startDate=&endDate=&sitegubun=&jisikgubun=&preKwd%5B0%5D=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5
#https://search.etnews.com/etnews/search.php?category=CATEGORY1&kwd=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&pageNum=2&pageSize=10&reSrchFlag=false&sort=1&startDate=&endDate=&sitegubun=&jisikgubun=&preKwd%5B0%5D=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5
#https://search.etnews.com/etnews/search.php?category=CATEGORY1&kwd=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&pageNum=3&pageSize=10&reSrchFlag=false&sort=1&startDate=&endDate=&sitegubun=&jisikgubun=&preKwd%5B0%5D=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5

#웹스크롤링에 필요한 모듈 임포트
from bs4 import BeautifulSoup
import urllib.request
import time
#중앙일보에서 인공지능으로 검색했을 때 나오는 첫페이지의 html코드를 BeautifulSoup에서 이용할 수 있도록 파싱
def jj_scroll():
    for h in range(1,4): #1~3 페이지만 가져오기
        list_url = 'https://search.etnews.com/etnews/search.php?category=CATEGORY1&kwd=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&pageNum='+str(h)+'&pageSize=10&reSrchFlag=false&sort=1&startDate=&endDate=&sitegubun=&jisikgubun=&preKwd%5B0%5D=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5'
        url=urllib.request.Request(list_url) 
        result=urllib.request.urlopen(url).read().decode("utf-8")
        soup=BeautifulSoup(result,"html.parser") #파싱해서 원하는 코드에 빨리 원하는 html에 접근할 수 있게 되었다.
        result1=soup.find_all('dt')
        params=[]
        for i in result1: #result1의 요소를 하나씩 빼낸다.
            for k in i: #h2태그 안의 a태그의 html코드를 가져오기 위한 코드
                params.append('http:'+k.get('href')) #a태그의 href의 값을 얻어내라
        return params

#기사들의 본문들을 가져오는 함수
def jj_detail_scroll():
    list_url = jj_scroll() #특정기사의 url을 쓰면 해당기사의 본문을 가져오지만 j_scroll()함수를 쓰면 함수안의 모든 기사의 url의 본문을 불러옴
    params2=[]
    for i in list_url: #list_url의 모든 url들을 읽어온다
        url=urllib.request.Request(i) 
        result=urllib.request.urlopen(url).read().decode("utf-8")
        soup=BeautifulSoup(result,"html.parser") 
        result1=soup.find_all(class_ ='article_body')
        for i in result1:
            #time.sleep(10)
            params2.append(i.get_text(" ",strip=True))
    return params2

print(jj_detail_scroll())
