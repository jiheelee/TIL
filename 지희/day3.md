## cloud 9

https://c9.io/jizzang?welcome

jizzang



### cloud에서 python 설치하기

https://github.com/pyenv/pyenv#installation



## 이메일보내기

```python
import smtplib
from email.message import EmailMessage

import getpass
password = getpass.getpass('비밀번호뭐니?')

msg = EmailMessage()
msg['subject'] = "제목은하하입니다"
msg['From'] = "dlwlgml8050@naver.com"
msg['To'] = "ohmyvia@naver.com"
msg.set_content('Hello')

smtp_url ='smtp.naver.com'
smtp_port = 465

s = smtplib.SMTP_SSL(smtp_url, smtp_port)

s.login('dlwlgml8050', password)
s.send_message(msg)
```

naver pop3 설정 사용함으로 바꾸기

## 

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>서버가 html도 보내주나???</h1>"
    
@app.route("/html_tag")
def html_tag():
    return """
    <h1>첫번째 줄!!!</h1>
    <h2>두번째 줄!!</h2>
    """

@app.route("/html_file")
def html_file():
    return render_template("html_file.html")
    
@app.route("/welcome/<string:name>")
def welcome(name):
    return render_template("welcome.html", people=name)

@app.route('/lotto')
def lotto():
    list = range(1,50)
    lot = random.sample(list,6)
    sort_lot = sorted(lot) #정렬 함수
    return render_template("lotto.html", lott = sort_lot)
```

## git에 올리는 작업

cd ..

cd "폴더이름"

new repository 생성

git init

git add .

git commit -m "커밋이름"

git link 넣기

git push -u origin master



## Append와 String formatting

```python
 week_format_num.append(lotto_dict["drwtNo{}".format(i)])
```

