from django.shortcuts import render,redirect
from AdminApp.models import CuisineDb
from AdminApp.models import DishDb
from WebApp.models import ContactDb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login


# Create your views here.
def index(req):
    return render(req,'index.html')
def AddCuisine(re):

    return render(re,'AddCuisine.html')
def SaveCuisine(re):
    a=re.POST.get('CuisineName')
    b=re.POST.get('Description')
    c=re.FILES['CuisineImage']
    aa=CuisineDb(CuisineName=a,Description=b,CuisineImage=c)
    aa.save()
    messages.success(re,"Cuisine saved!")
    return redirect('AddCuisine')
def DisplayCuisine(re):
    data=CuisineDb.objects.all()
    return render(re,'DisplayCuisine.html',{'data':data})

def EditCuisine(re,E_id):
    dat=CuisineDb.objects.get(id=E_id)
    return render(re,'EditCuisine.html',{'dat':dat})
def UpdateCuisine(re,U_id):
    a1=re.POST.get('CuisineName')
    b1=re.POST.get('Description')
    try:
      c1=re.FILES['CuisineImage']
      fs=FileSystemStorage()
      file=fs.save(c1.name,c1)
    except MultiValueDictKeyError:
      file=CuisineDb.objects.get(id=U_id).CuisineImage
    CuisineDb.objects.filter(id=U_id).update(CuisineName=a1,Description=b1,CuisineImage=file)
    return redirect('DisplayCuisine')

def DeleteCuisine(re,D_id):
    obj=CuisineDb.objects.filter(id=D_id)
    obj.delete()
    messages.error(re, "Cuisine removed!")
    return redirect('DisplayCuisine')


# Dishes

def AddDish(re):
    cat=CuisineDb.objects.all()
    return render(re,'AddDishes.html',{'cat':cat})
def SaveDish(re):
    a2=re.POST.get('Cuisine')
    b2=re.POST.get('DishName')
    c2=re.POST.get('Price')
    d2=re.POST.get('About')
    e2=re.FILES['DishImage']
    aa2=DishDb(Cuisine=a2,DishName=b2,Price=c2,About=d2,DishImage=e2)
    aa2.save()
    messages.success(re, "Dish added!")
    return redirect('AddDish')
def DisplayDish(re):
    cd=DishDb.objects.all()
    return render(re,'DisplayDish.html',{'cd':cd})
def EditDishes(re,Ed_id):
    ed=DishDb.objects.get(id=Ed_id)
    cat=CuisineDb.objects.all()
    return render(re,'EditDish.html',{'ed':ed,'cat':cat})
def UpdateDish(re,UD_id):
    a22=re.POST.get('Cuisine')
    b22=re.POST.get('DishName')
    c22=re.POST.get('Price')
    d22=re.POST.get('About')
    try:
     e22=re.FILES['DishImage']
     fs=FileSystemStorage()
     file=fs.save(e22.name,e22)
    except MultiValueDictKeyError:
     file=DishDb.objects.get(id=UD_id).DishImage
    DishDb.objects.filter(id=UD_id).update(Cuisine=a22, DishName=b22, Price=c22, About=d22, DishImage=file)
    return redirect('DisplayDish')

def DeleteDish(re,DD_id):
    dd=DishDb.objects.filter(id=DD_id)
    dd.delete()
    messages.error(re, "Dish removed!")
    return redirect('DisplayDish')

def Login(request):
    return render(request,'Login.html')

def AdminLogin(request):
    if request.method=='POST':
        un=request.POST.get('UserName')
        pswd=request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pswd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pswd
                return redirect(index)
            else:
                return redirect(Login)
        else:
            return redirect(Login)

def admin_logout(request):
    if 'username' in request.session:
        del request.session['username']
    if 'password' in request.session:
        del request.session['password']
    return redirect(Login)
def ContactDetails(re):
    Co=ContactDb.objects.all()
    return render(re,'ContactDetails.html',{'Co':Co})
def DeleteContact(re,D):
    De=ContactDb.objects.get(id=D)
    De.delete()
    return redirect(ContactDetails)



