from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import * 

def form(request):
    if request.method=='POST':
        tn=request.POST['tn']
        to=Topic.objects.get_or_create(Topic_name=tn)[0]
        to.save()
        return  HttpResponse('inserted successfully')
    return render(request,'form.html')
def webpage(request):
    if request.method=='POST':
        tn=request.POST['tn']
        ne=request.POST.get('ne')
        ur=request.POST.get('ur')
        to=Topic.objects.get(Topic_name=tn)
        wo=Webpage.objects.get_or_create(Topic_name=to,Name=ne,Url=ur)[0]
        wo.save()
        return HttpResponse('inserted successfully')
    top=Topic.objects.all()
    d={'topic':top}
    return render(request,'webpage.html',d)
def accesspage(request):
    if request.method=='POST':
        ne=request.POST['ne']
        au=request.POST['au']
        da=request.POST['da']
        ne=Webpage.objects.get(Name=ne)
        ao=Access.objects.get_or_create(Name=ne,Author=au,Date=da)[0]
        ao.save()
        return HttpResponse('inserted successfully')
    wop=Webpage.objects.all()
    d={'name':wop}
    return render(request,'accesspage.html',d)
def retriou(request):
    top=Topic.objects.all()
    d={'topic':top}
    if request.method=='POST':
        tn=request.POST.getlist('tn')
        webset=Webpage.objects.none()
        for i in tn:
            webset=webset|Webpage.objects.filter(Topic_name=i)
        d1={'topic':webset}
        return render(request,'display.html',d1)
    return render(request,'retriou.html',d)
    
def checkbox(request):
    top=Topic.objects.all()
    d={'topic':top}
    return render(request,'checkbox.html',d)
def accessretreve(request):
    nop=Webpage.objects.all()
    d2={'webpage':nop}
    if request.method=='POST':
        ne=request.POST.getlist('ne')
        print(ne)
        query=Access.objects.none()
        for i in ne:
            query=query|Access.objects.filter(Name=i)
        d3={'access':query}
        return render(request,'accessview.html',d3)

    return render(request,'accessretreve.html',d2)
def updating(request):
    dop=Webpage.objects.all()
    d2={'webpage':dop}
    if request.method=='POST':
        ne=request.POST.get('ne')
        up=request.POST.get('up')
        Webpage.objects.filter(Name=ne).update(Url=up)
        ko=Webpage.objects.all()
        d1={'topic':ko}
        return render(request,'display.html',d1)
    return render(request,'updating.html',d2)
def deleting(request):
    nop=Access.objects.all()
    d2={'webpage':nop}
    if request.method=='POST':
        ne=request.POST.get('ne')
        Access.objects.filter(Name=ne).delete()
        ao=Access.objects.all()
        d={'access':ao}
        return render(request,'accessview.html',d)
    
    return render(request,'accessretreve.html',d2)