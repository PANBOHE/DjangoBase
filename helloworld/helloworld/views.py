from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world!")

def runnoob(request):
    context = {}
    context['hello'] = "hello my world!"
    return render(request, "runnoob.html", context)

def runmuban(request):
    #context = {}
    #context["name"] = "my test data!"
    views_name = "My test data to show!"
    #views_list = ["My data1", "My data2", "My data3"]
    views_dict = {"name":"my test dict data "}
    return render(request, "mytestdata.html", {"views_list":views_dict})


def panbouse(request):
    infor = "here is panbo information"
    return render(request,infor)
