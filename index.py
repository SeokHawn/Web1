#!C:\Users\Seokhawn\anaconda3\python
import sys
import codecs
import cgi, os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) # 한글 출력을 위한 Encoding


print("content-type: text/html") #print pay load
print() # print endline

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form['id'].value
    description = open('data/' + pageId, 'r',encoding='utf-8').read()
else:
    pageId = 'Welcome'
    description = 'Hello, Web'

files = os.listdir('data')
listStr=''
for item in files:
    listStr = listStr + '<li> <a href="index.py?id={name}">{name}</a></li>'.format(name=item)

print('''<!doctype html>
<html>
<head>
  <title>WEB1 - HTML</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
    <ol>
      {listStr}
    </ol>
<h2>{title}</h2>
<p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc = description, listStr = listStr))
