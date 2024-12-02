from django.shortcuts import render,redirect
from WebApp.models import ContactDb,SignUpDb,CartDb,OrderDb
# Create your views here.
from AdminApp.models import CuisineDb,DishDb
from django.contrib import messages

def Home(re):
    Cu = CuisineDb.objects.all()
    cart=CartDb.objects.count()
    return render(re,'Home.html',{'Cu':Cu,'cart':cart})
def About(re):
    cart=CartDb.objects.count()
    return render(re,'About.html',{'cart':cart})
def Contact(re):
    cart = CartDb.objects.count()
    return render(re,'Contact.html',{'cart':cart})
def SaveContact(re):
    a=re.POST.get('Name')
    b=re.POST.get(' Email')
    c=re.POST.get('Subject')
    d=re.POST.get('Message')
    obj=ContactDb(Name=a,Email=b,Subject=c,Message=d)
    obj.save()
    messages.success(re,"Contact saved")
    return redirect(Contact)
def DishesFiltered(re,CName):
    data=DishDb.objects.filter(Cuisine=CName)
    cart = CartDb.objects.count()
    return render(re,'DishesFiltered.html',{'data':data,'cart':cart})
def Dishes(re):
    Menu=DishDb.objects.all()
    return render(re,'Dishes.html',{'Menu':Menu,'cart':cart})
def SingleDish(re,Di):
    dish=DishDb.objects.get(id=Di)
    cart =CartDb.objects.count()
    return render(re,'SingleDish.html',{'dish':dish,'cart':cart})
def SignUp(re):
    return render(re,'SignUp.html')

def SaveSignUp(re):
    a1=re.POST.get('name')
    b1=re.POST.get('email')
    c1=re.POST.get('mobile')
    d1=re.POST.get('pass1')
    e1=re.POST.get('re_pass')
    obj=SignUpDb(name=a1,email=b1,mobile=c1,pass1=d1,re_pass=e1)
    obj.save()
    return redirect(Home)

def SignIn(re):
    return render(re,'SignIn.html')

def UserLogin(request):
    if request.method=='POST':
        un=request.POST.get('name')
        pwd=request.POST.get('pass1')
        if SignUpDb.objects.filter(name=un,pass1=pwd).exists():
            request.session['name']=un
            request.session['pass1']=pwd
            return redirect(Home)
        else:
            return redirect(SignIn)
    else:
        return redirect(SignIn)

def UserLogout(request):
    del request.session['name']
    del request.session['pass1']
    return redirect(SignIn)

def CartSave(re):
    if re.method=='POST':
        a5=re.POST.get('name')
        b5=re.POST.get('DishName')
        c5=re.POST.get('Price')
        d5=re.POST.get('Quantity')
        e5=re.POST.get('Total')
        obj=CartDb(name=a5,DishName=b5,Price=c5,Quantity=d5,Total=e5)
        obj.save()
        return redirect(Checkout)

def Checkout(re):
    items=CartDb.objects.filter(name=re.session['name'])
    cart1=CartDb.objects.filter(name=re.session['name'])
    SubTotal = 0
    ShippingAmount = 0
    TotalAmount = 0
    for i in items:
        SubTotal = SubTotal + i.Total
        if SubTotal > 1000:
            ShippingAmount = 60
        else:
            ShippingAmount = 160
        TotalAmount = ShippingAmount + SubTotal
        cart = CartDb.objects.count()
    return render(re, 'Checkout.html',{'items':items,'cart1':cart1,'SubTotal': SubTotal, 'ShippingAmount': ShippingAmount, 'TotalAmount': TotalAmount,'cart':cart})


def CartsPage(re):
    cart1=CartDb.objects.filter(name=re.session['name'])
    SubTotal=0
    ShippingAmount=0
    TotalAmount=0
    for i in cart1:
        SubTotal=SubTotal+i.Total
        if SubTotal>1000:
            ShippingAmount=60
        else:
            ShippingAmount=160
        TotalAmount=ShippingAmount+SubTotal
        cart = CartDb.objects.count()
    return render(re,'Cart.html',{'cart1':cart1,'SubTotal':SubTotal,'ShippingAmount':ShippingAmount,'TotalAmount':TotalAmount,'cart':cart})

def CartRemove(re,D_id):
    x=CartDb.objects.filter(id=D_id)
    x.delete()
    return redirect(CartsPage)
def OrderSave(re):
    a=re.POST.get('name')
    b=re.POST.get('email')
    c=re.POST.get('Mobile')
    d=re.POST.get('DishName')
    e=re.POST.get('Quantity')
    f=re.POST.get('Price')
    g=re.POST.get('TotalAmount')
    h=re.POST.get('Address')
    obj=OrderDb(name=a,email=b,Mobile=c,DishName=d,Quantity=e,Price=f,TotalAmount=g,Address=h)
    obj.save()
    return redirect(Payment)

def Payment(re):
    # Retrieve the data from OrderDb with the specified ID in reverse order

    customer = OrderDb.objects.order_by('-id').first()

    # Get the payment amount of the specified customer

    pay = customer.TotalAmount
    # convert the amount into paisa(Smallest currency unit)
    amount = int(pay * 100)
    pay_str = str(amount)

    for i in pay_str:
        print(i)
        if re.method == "POST":
            order_currency = 'INR'
            client = razorpay.Client(auth=('your_key', 'your_id'))
            payment = client.order.create({'amount': amount, 'currency': order_currency})
        return render(re, 'Payment.html', {'customer': customer, 'pay_str': pay_str})
