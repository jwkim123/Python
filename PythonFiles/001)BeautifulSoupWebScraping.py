# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 09:49:34 2020
@author: jw
"""
#%%
#beautifulsoup 연습-1
from bs4 import BeautifulSoup
f=open("d:\\data\\ecologicalpyramid.html")
soup=BeautifulSoup(f,"html.parser")
print(soup)

#%%
#ecologicalpyramid에서 class이름 name에 접근해서 데이터를 긁어오시오
from bs4 import BeautifulSoup
f=open("d:\\data\\ecologicalpyramid.html")
soup=BeautifulSoup(f,"html.parser")
result=soup.find_all(class_ ="name")
print(result)

#%%
#위에서 긁어온 데이터에서 html코드말고 text만 출력하기
from bs4 import BeautifulSoup
f=open("d:\\data\\ecologicalpyramid.html")
soup=BeautifulSoup(f,"html.parser")
result=soup.find_all(class_ ="name")
for i in result: #result리스트 안의 요소를 하나씩 가져옵니다.
    print(i.get_text())
    
#%%
#Q.ecologicalpyramid에서 class 이름 number의 숫자만 가져와서 a라는 비어있는 리스트에 
#저장한 후 a안의 요소들을 정렬하고 a리스트를 출력하시오
from bs4 import BeautifulSoup
f=open("d:\\data\\ecologicalpyramid.html")
soup=BeautifulSoup(f,"html.parser")
result=soup.find_all(class_ ="number")
a=[]
for i in result: #result리스트 안의 요소를 하나씩 가져옵니다.
    a.append(int(i.get_text()))
a.sort()
print(a)
    
#%%
#Q.중앙일보에서 기사 하나를 html로 저장하고 파싱하시오
from bs4 import BeautifulSoup
f=open("d:\\data\\aa77.html", encoding='UTF8')
soup=BeautifulSoup(f,"html.parser")
print(soup)

#%%
#Q.위의 기사에서 본문에 해당하는 class 이름을 찾아서 해당 클래스의 text를 긁어오시오
from bs4 import BeautifulSoup
f=open("d:\\data\\aa77.html", encoding='UTF8')
soup=BeautifulSoup(f,"html.parser")
result=soup.find_all(class_ ="article_body mg fs4")
for i in result: #result리스트 안의 요소를 하나씩 가져옵니다.
    print(i.get_text())
    
#%%
#Q.중앙일보에서 기사를 하나 스크롤링 해오고 mytext23.txt라는 파일을 생성하시오
from bs4 import BeautifulSoup
f=open("d:\\data\\aa77.html", encoding='UTF8')
soup=BeautifulSoup(f,"html.parser")
result=soup.find_all(class_ ="article_body mg fs4")
a=[]
for i in result: #result리스트 안의 요소를 하나씩 가져옵니다.
    a.append(i.get_text())
    
with open("d:\\data\\mytext23.txt","w", encoding='UTF8') as f:#mydata2.txt를 생성하겠다.
    data=f.write(str(a)) #result에 있는 내용을 문자열로 변환해서 mydata2.txt로 생성한다.
    
    
#기사출처: 김정민 . “[팩플]'베테랑 전문의' AI 의사, 한국은 100대 기업에 못 든다고?” 중앙일보, 중앙일보, 14 Dec. 2020, news.joins.com/article/23945435.
