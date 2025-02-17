from django.shortcuts import render

from django.http import HttpResponse
#def index(request):
#   return HttpResponse("Hello, world!")


def index1(request):
    name = request.GET.get("name") or "world!"
    return HttpResponse("Hello, "+name)
 
def index2(request, val1 = 0):   
    return HttpResponse("value1 = "+str(val1))

#def index(request): 
    #name = request.GET.get("name") or "world!"
    #return render(request, "bookmodule/index.html")    

 
def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html" , {"name": name})  
