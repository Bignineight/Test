from django.shortcuts import render
from django.http import HttpResponse
from web.models import Douban_top
from web.models import tianqi_sun
from web.models import jingdong_test
from django.core.paginator import Paginator

# Create your views here.  视图处理的地方

def index(request):
    return render(request,'1.html',{})

def douban_content(request):
    douban=Douban_top.objects.all()
    
    return render(request,'2.html',{ 'douban':douban})

def tianqi_content(request):
    tianqi=tianqi_sun.objects.all()

    return render(request,'3.html',{ 'tianqi':tianqi})

def jingdong_content(request):
    jingdong=jingdong_test.objects.all()

    return render(request,'4.html',{ 'jingdong':jingdong})