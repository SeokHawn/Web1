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
    <a href = "create.py">create</a>
    <form action="process_update.py" method="post">
        <input type="hidden" name = "pageId" value="{form_default_title}">
        <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
        <p><textarea rows="4" name="description" placeholder="description">{form_default_description}</textarea></p>
        <p><input type="submit"></p>
    </form>
</body>
</html>
'''.format(title=pageId, desc = description, listStr = listStr, form_default_title = pageId, form_default_description = description)) #name : server로 전송한 데이터의 이름
                                                                 #package로 tag를 달아서 application(action에 들어간 이름의 어플리케이션)으로 전송할 때, "form"을 사용함.
