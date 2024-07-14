from django.shortcuts import render,HttpResponse
from .models import Author,category
# Create your views here.
def first(request):
    return HttpResponse("this is my first view function..")


def second(request):
    return render(request,'first.html')

def table(request):
    authordata = Author.objects.all()
    # print(authordata)
    # i = name:a , email:a@gmail.com , i = name:b , email:b@gmail.com 
    # for i in authordata:
    #     print(i.name)
    #     print(i.email)
    return render(request,'table.html',{'author':authordata})

def cattable(request):
    storecat = category.objects.all()
    return render(request,'cattable.html',{'catdata':storecat})


def form(request):
    if request.method == 'POST':
        print(11111)
        storeauthor = Author()
        storeauthor.name = request.POST['uname']
        storeauthor.email = request.POST['email']
        storeauthor.save()
    # print(22222)
        return render(request,'form.html')
    else:
        return render(request,'form.html')
        # return HttpResponse("data not submitted")


def catform(request):
    if request.method == 'POST' and request.FILES['img']:
        storecat = category()
        storecat.name = request.POST['catname']
        storecat.image = request.FILES['img']
        storecat.save()
        return render(request,'catform.html')
    else:
        return render(request,'catform.html')


def update(request):
    try:
        if request.method == 'POST':
            print(111111111111)
            # a = Author()
            # a.name = request.POST['uname']
            authordata = Author.objects.get(name = 'd')
            authordata.name = request.POST['uname']
            authordata.email = request.POST['email']
            authordata.save()
            return render(request,'update.html',{'author':authordata})
        else:
            authordata = Author.objects.get(name = 'd')
            return render(request,'update.html',{'author':authordata})
    except Exception as e:
    #     print(2222222222222)
        return render(request,'update.html')
        

def index(request):
    
    catdata = category.objects.all()
    return render(request,'index.html',{'cat':catdata})
