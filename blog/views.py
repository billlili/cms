#from django.http import HttpResponse
#from django.template import loader,Context
from django.shortcuts import render_to_response
# Create your views here.
'''def index(req):
    t=loader.get_template('index.html')
    c=Context({})

    return HttpResponse(t.render(c))
'''
class Person(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def say(self):
        return "I'm "+self.name

def index(req):
    #user={'name':'lihongjiao','age':'26','sex':'mmZle'}
    user=Person('lihongjiao',26,'male')
    book_list=['python','java','php','web']
    return render_to_response('index.html',{'title':'my page','book_list':book_list})
