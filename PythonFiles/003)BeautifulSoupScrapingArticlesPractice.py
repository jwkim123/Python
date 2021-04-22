# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 11:12:09 2020
@author: jw
"""
#%%
#BeautifulSoup실전2-중앙일보사 홈페이지에서 인공지능으로 검색하고 url을 가져오시오
#웹스크롤링에 필요한 모듈 임포트
from bs4 import BeautifulSoup
import urllib.request
#중앙일보에서 인공지능으로 검색했을 때 나오는 첫페이지의 html코드를 BeautifulSoup에서 이용할 수 있도록 파싱
list_url = "https://news.joins.com/Search/JoongangNews?page=1&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=JoongangNews"
url=urllib.request.Request(list_url) 
result=urllib.request.urlopen(url).read().decode("utf-8")
soup=BeautifulSoup(result,"html.parser") #파싱해서 원하는 코드에 빨리 원하는 html에 접근할 수 있게 되었다.
print(soup)

#%%
#BeautifulSoup실전2-상세기사의 태그와 클래스를 가져오시오
#웹스크롤링에 필요한 모듈 임포트
from bs4 import BeautifulSoup
import urllib.request
#중앙일보에서 인공지능으로 검색했을 때 나오는 첫페이지의 html코드를 BeautifulSoup에서 이용할 수 있도록 파싱
list_url = "https://news.joins.com/Search/JoongangNews?page=1&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=JoongangNews"
url=urllib.request.Request(list_url) 
result=urllib.request.urlopen(url).read().decode("utf-8")
soup=BeautifulSoup(result,"html.parser") #파싱해서 원하는 코드에 빨리 원하는 html에 접근할 수 있게 되었다.
result1=soup.find_all('h2',class_ ='headline mg')
print(result1)

#%%
#BeautifulSoup실전2-위의 result1은 리스트 이므로 for loop을 이용해서 리스트의 요소를 하나씩 꺼내면서 상세 url들만 가져오시오(href)
#웹스크롤링에 필요한 모듈 임포트
from bs4 import BeautifulSoup
import urllib.request
#중앙일보에서 인공지능으로 검색했을 때 나오는 첫페이지의 html코드를 BeautifulSoup에서 이용할 수 있도록 파싱
list_url = "https://news.joins.com/Search/JoongangNews?page=1&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=JoongangNews"
url=urllib.request.Request(list_url) 
result=urllib.request.urlopen(url).read().decode("utf-8")
soup=BeautifulSoup(result,"html.parser") #파싱해서 원하는 코드에 빨리 원하는 html에 접근할 수 있게 되었다.
result1=soup.find_all('h2',class_ ='headline mg')
for i in result1: #result1의 요소를 하나씩 빼낸다.
    for k in i: #h2태그 안의 a태그의 html코드를 가져오기 위한 코드
        print(k.get('href')) #a태그의 href의 값을 얻어내라

#%%
#BeautifulSoup실전2-위의 결과의 상세기사 url들을 params라는 비어있는 리스트에 append하시오
#웹스크롤링에 필요한 모듈 임포트
from bs4 import BeautifulSoup
import urllib.request
#중앙일보에서 인공지능으로 검색했을 때 나오는 첫페이지의 html코드를 BeautifulSoup에서 이용할 수 있도록 파싱
list_url = "https://news.joins.com/Search/JoongangNews?page=1&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=JoongangNews"
url=urllib.request.Request(list_url) 
result=urllib.request.urlopen(url).read().decode("utf-8")
soup=BeautifulSoup(result,"html.parser") #파싱해서 원하는 코드에 빨리 원하는 html에 접근할 수 있게 되었다.
result1=soup.find_all('h2',class_ ='headline mg')
params=[]
for i in result1: #result1의 요소를 하나씩 빼낸다.
    for k in i: #h2태그 안의 a태그의 html코드를 가져오기 위한 코드
        params.append(k.get('href')) #a태그의 href의 값을 얻어내라
print(params)

#%%
#BeautifulSoup실전2-상세기사의 태그와 클래스를 찾고 텍스트만 추출하여 params2라는 빈 리스트에 담으시오
#웹스크롤링에 필요한 모듈 임포트
from bs4 import BeautifulSoup
import urllib.request
#중앙일보에서 상세기사 url로 검색했을 때 나오는 첫페이지의 html코드를 BeautifulSoup에서 이용할 수 있도록 파싱
list_url = "https://news.joins.com/article/23947044"
url=urllib.request.Request(list_url) 
result=urllib.request.urlopen(url).read().decode("utf-8")
soup=BeautifulSoup(result,"html.parser") #파싱해서 원하는 코드에 빨리 원하는 html에 접근할 수 있게 되었다.
#상세기사의 본문을 가져올 수 있도록 태그와 클래스를 찾는다. 태그div, 클래스 article_body mg fs4
result1=soup.find_all('div',class_ ='article_body mg fs4')
#위의 result1은 리스트이므로 forloop문을 이용해서 리스트에 있는 요소를 하나씩 빼내면서 본문의 텍스트를 얻어냅니다.
params2=[]
for i in result1: #result1의 요소를 하나씩 빼낸다.
    params2.append(i.get_text(" ",strip=True)) #a태그의 href의 값을 얻어내라
print(params2)

#%%
#BeautifulSoup실전2-위의 상세기사 url을 출력하는 코드를 함수로 생성하기
#웹스크롤링에 필요한 모듈 임포트
from bs4 import BeautifulSoup
import urllib.request
#중앙일보에서 인공지능으로 검색했을 때 나오는 첫페이지의 html코드를 BeautifulSoup에서 이용할 수 있도록 파싱
def j_scroll():
    list_url = "https://news.joins.com/Search/JoongangNews?page=1&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=JoongangNews"
    url=urllib.request.Request(list_url) 
    result=urllib.request.urlopen(url).read().decode("utf-8")
    soup=BeautifulSoup(result,"html.parser") #파싱해서 원하는 코드에 빨리 원하는 html에 접근할 수 있게 되었다.
    result1=soup.find_all('h2',class_ ='headline mg')
    params=[]
    for i in result1: #result1의 요소를 하나씩 빼낸다.
        for k in i: #h2태그 안의 a태그의 html코드를 가져오기 위한 코드
            params.append(k.get('href')) #a태그의 href의 값을 얻어내라
    return params

print(j_scroll())

#%%
#BeautifulSoup실전2-상세기사 본문을 리스트에 담았던 코드를 함수로 생성하시오
#웹스크롤링에 필요한 모듈 임포트
from bs4 import BeautifulSoup
import urllib.request
    #중앙일보에서 상세기사 url로 검색했을 때 나오는 첫페이지의 html코드를 BeautifulSoup에서 이용할 수 있도록 파싱
def j_detail_scroll():
    list_url = "https://news.joins.com/article/23947044"
    url=urllib.request.Request(list_url) 
    result=urllib.request.urlopen(url).read().decode("utf-8")
    soup=BeautifulSoup(result,"html.parser") #파싱해서 원하는 코드에 빨리 원하는 html에 접근할 수 있게 되었다.
    #상세기사의 본문을 가져올 수 있도록 태그와 클래스를 찾는다. 태그div, 클래스 article_body mg fs4
    result1=soup.find_all('div',class_ ='article_body mg fs4')
    #위의 result1은 리스트이므로 forloop문을 이용해서 리스트에 있는 요소를 하나씩 빼내면서 본문의 텍스트를 얻어냅니다.
    params2=[]
    for i in result1: #result1의 요소를 하나씩 빼낸다.
        params2.append(i.get_text(" ",strip=True)) #a태그의 href의 값을 얻어내라
    return params2

print(j_detail_scroll())

#%%
#BeautifulSoup실전2-
#웹스크롤링에 필요한 모듈 임포트
from bs4 import BeautifulSoup
import urllib.request
#기사들의 url을 가져오는 함수
def j_scroll():
    list_url = "https://news.joins.com/Search/JoongangNews?page=1&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=JoongangNews"
    url=urllib.request.Request(list_url) 
    result=urllib.request.urlopen(url).read().decode("utf-8")
    soup=BeautifulSoup(result,"html.parser") 
    result1=soup.find_all('h2',class_ ='headline mg')
    params=[]
    for i in result1: 
        for k in i: 
            params.append(k.get('href'))
    return params

#기사들의 본문들을 가져오는 함수
def j_detail_scroll():
    list_url = j_scroll() #특정기사의 url을 쓰면 해당기사의 본문을 가져오지만 j_scroll()함수를 쓰면 함수안의 모든 기사의 url의 본문을 불러옴
    params2=[]
    for i in list_url: #list_url의 모든 url들을 읽어온다
        url=urllib.request.Request(i) 
        result=urllib.request.urlopen(url).read().decode("utf-8")
        soup=BeautifulSoup(result,"html.parser") 
        result1=soup.find_all('div',class_ ='article_body mg fs4')
        for i in result1:
            params2.append(i.get_text(" ",strip=True))
    return params2

print(j_detail_scroll())
