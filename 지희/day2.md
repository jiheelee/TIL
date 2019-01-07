git for windows



python 3.6.7



codevs



python 





student@DESKTOP MINGW64 ~/jihee
$ python -V (버전)
Python 3.6.7

student@DESKTOP MINGW64 ~/jihee
$ mkdir haha ( 폴더 만들기 )



## Web Browser

```python
import webbrowser

url="https://google.com"

webbrowser.open(url)



import webbrowser

url="https://google.com"

url="https://www.google.com/search?&q="

webbrowser.open(url+"SSAFY(바꿀수있음)")
```





### 한번에 여러개

```python
import webbrowser

q_list = ["bts","아이유","블랙핑크","위너"]

url="https://www.google.com/search?&q="

for q in q_list:

    webbrowser.open(url+q)

#리스트 만들어서 반복문으로 돌리기
```





### Web crawling

pip install requests (bs4) - 설치해줘야함

<hello 출력>

```python
import requests

print("hello")

python crawling.py



import requests

url= "https://google.com"

res = requests.get(url) (객체->정보가 담겨있음)

res = requests.get(url).text (텍스트)

res = requests.get(url).status_code (코드)

print(res)
```



### 끌어오기

```python
import requests
from bs4 import BeautifulSoup

url= "https://www.daum.net/"
#res = requests.get(url).status_code
res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')
pick= soup.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li:nth-of-type(3) > div > div:nth-of-type(2) > span.txt_issue > a') #child를 -of-type으로 바꾸기
print(pick)

<모든 검색순위>
#'#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li (모든 검색순위)> div > div:nth-of-type(1) > span.txt_issue > a'


<for문으로 깔끔하게>
picks= soup.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li > div > div:nth-of-type(1) > span.txt_issue > a')
for p  in picks:
    print(p.text)->텍스트만
```

#있으면 아이디, (.)있으면 클래스

```python
import requests
from bs4 import BeautifulSoup
url= "http://m.exchange.daum.net/mobile/exchange/exchangeMain.daum"

res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')

picks= soup.select('#asiaBody > table tr.link')
for p in picks:
    # print(p.select_one("td.name").text)

    print(p.select_one("td.name a").text)
    print(p.select_one("td.idx").text)
    print("--------------------")
  
```



https://gist.github.com/eduChang/ab52b31e228934ac05992b83319c769b

-> 권한 없는 사이트 긁어오기

<파일 이름 바꾸기>

```python
import os

os.chdir(r'C:\Users\student\jihee\SSAFY지원자')

for filename in os.listdir("."):
    new_filename = filename.replace("SAMSUNG","SSAFY")
    os.rename(filename, new_filename)
```



git init - git 관리 구조

 git add python.py - 파일 추가



  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

$ git commit -m "python.py 추가함"

$ git add .



블로그 만들기

jiheelee.github.io

폴더 열기(탬플릿)





1. git init
2. git add .
3. git commit -m " 메세지"

4. remote
5. push

