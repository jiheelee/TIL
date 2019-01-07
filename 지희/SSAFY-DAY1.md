# SSAFY-DAY1

## 첫번째 시간



### PYTHON 코드 작성(광주먼지)

```PYTHON
import requests
from bs4 import BeautifulSoup
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=' + key + '&numOfRows=10&pageSize=10&pageNo=1&startPage=1&sidoName=%EA%B4%91%EC%A3%BC&ver=1.3'
request = requests.get(url).text
soup = BeautifulSoup(request,'xml')
dong = soup('item')[7]
location = dong.stationName.text
time = dong.dataTime.text
dust = int(dong.pm10Value.text)

print("{0} 기준 {1}의 미세먼지 농도는 {2}입니다.".format(time,location,dust))

if dust >150:
  print("매우나쁨")
elif dust > 80:
  print("나쁨")
elif dust > 50:
  print("보통")
else:
  print("좋음")
  
  

```

### PYTHON 코드 작성(FOR)

```python
a= [1,2,3,4,5]
for i in a:
  print("안녕하세요")
```

### LOTTO

```python
import random
lotto = list(range(1,46))
a = random.sample(lotto,6)
print(a)
```

### KOSPI

```python
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
r = requests.get(url).text
soup = BeautifulSoup(r,'html.parser')
select = soup.select_one("#KOSPI_now")
print(select.text)

```

