#from django.http import HttpResponse
#from django.template import RequestContext,loader
from django.shortcuts import get_object_or_404,render
#from django.http import Http404,HttpResponse 
from poll.models import Question

def index(request):
    latest_question_list=Question.objects.all().order_by('-pub_date')[:5]
    context={'latest_question_list':latest_question_list}
    return render(request,'poll/index.html',context)
def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'poll/detail.html',{'question':question})


#def index(request):
#    latest_question_list=Question.objects.order_by('-pub_date')[:5]
#    template=loader.get_template('poll/index.html')
#    context=RequestContext(request,{'latest_question_list':latest_question_list,
#    })
#    return HttpResponse(template.render(context))

#def detail(request,question_id):
#    return HttpResponse("You're looking at question %s" %question_id)

def results(request,question_id):
    response="You're looking at the results of question %s."
    return HttpResponse(response %question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s." %question_id)
