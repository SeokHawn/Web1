import os

# define을 사용하여 모듈화 작업

def getList():
    files = os.listdir('data')
    listStr=''
    for item in files:
        listStr = \
        listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

    return listStr
