#!C:\Users\Seokhawn\anaconda3\python
import sys
import codecs
import cgi, os, view
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) # 한글 출력을 위한 Encoding


print("content-type: text/html") #print pay load - 지금 부터 작업할 내용은 text이고 html언어야!
print() # print endline


form = cgi.FieldStorage()
if 'id' in form:
    pageId = form['id'].value
    description = open('data/' + pageId, 'r',encoding='utf-8').read()
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action ='''
        <form action="process_delete.py" method="post">
            <input type ="hidden" name = "pageId" value ="{}">
            <input  type ="submit" value="delete">
        </form>
    '''.format(pageId)
else:
    pageId = 'Welcome'
    description = 'Hello, Web'
    update_link=''
    delete_action=''


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
    {update_link}
    {delete_action}
    <h2>{title}</h2>
    <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc = description, listStr = view.getList(),
 update_link = update_link, delete_action= delete_action))
