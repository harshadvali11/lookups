from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.db.models.functions import Length

from app.models import *
def insert_topic(request):
    t=Topic.objects.get_or_create(topic_name='Kabaddi')[0]
    t.save()
    return HttpResponse('Topic is added successg=fully')

def insert_webpage(request):
    t1=Topic.objects.get_or_create(topic_name='Kabaddi')[0]
    t1.save()
    w=Webpage.objects.get_or_create(topic_name=t1,name='JPG',url='https://jpg.com')[0]
    w.save()
    return HttpResponse('WEbpage data is inserted')

def display_topics(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    LOW=Webpage.objects.all()
    #LOW=Webpage.objects.filter(topic_name='V Ball')
    #LOW=Webpage.objects.exclude(topic_name='V Ball')
    #LOW=Webpage.objects.all()[:5:]
    LOW=Webpage.objects.all().order_by('name')  
    LOW=Webpage.objects.all().order_by('-name')
    LOW=Webpage.objects.all().order_by(Length('name'))
    LOW=Webpage.objects.all().order_by(Length('name').desc())
    
    d={'webpages':LOW}
    return render(request,'display_webpages.html',d)

def display_access(request):
    LOA=Access_Records.objects.all()
    LOA=Access_Records.objects.filter(date='1990-01-12')
    LOA=Access_Records.objects.filter(date__gte='1990-01-12')
    LOA=Access_Records.objects.filter(date__lte='1990-01-12')
    LOA=Access_Records.objects.filter(date__year='1980')
    LOA=Access_Records.objects.filter(date__month='01')
    LOA=Access_Records.objects.filter(date__day='12')
    LOA=Access_Records.objects.filter(date__year__gt='1990')
    
    
    
    
    d={'access':LOA}
    return render(request,'display_access.html',d)


















