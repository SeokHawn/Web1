#!C:\Users\Seokhawn\anaconda3\python
import sys
import codecs
import cgi
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) # 한글 출력을 위한 Encoding

print("content-type: text/html") #print pay load
print() # print endline

form = cgi.FieldStorage()
pageId = 'Welcome'
if("id" in form):
    pageId = form["id"].value
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - HTML</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
    <ol>
      <li> <a href="index.py?id=HTML">HTML</a></li>
      <li> <a href="index.py?id=CSS">CSS</a></li>
      <li> <a href="index.py?id=JavaScript">JavaScript</a></li>
    </ol>
<h2>{title}</h2>
<p>
1989년 12월 16일에 개발되고 1990년 12월 20일에 발표 및 보급된
월드 와이드 웹(World Wide Web, WWW, W3)은 인터넷에 연결된 컴퓨터를 이용해 사람들과
 정보를 공유할 수 있는 거미줄(Web)처럼 얼기설기 엮인 공간을 뜻하는 용어다.
 HTTP 프로토콜을 기반으로 HTML로 작성된 하이퍼텍스트 페이지를 웹 브라우저라는
  특정한 프로그램으로 읽을 수 있게 하도록 구성되어 있다. WWW, W3, 또는
  간단하게 웹(Web)이라고도 한다. 일반인에게 인터넷이 보급되기 시작한 1994년부터
   사실상 인터넷과 동의어 취급할 정도로 가장 널리 보급된 인터넷 시스템이다.
   일반인들에게 인터넷 한다는 게 뭐냐고 물어보면 대다수는 웹 브라우저 켜고
   웹 서핑하는 것이라고 대답할 것이다.
</p>
</body>
</html>
'''.format(title=pageId))
