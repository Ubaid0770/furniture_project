from django.shortcuts import render,redirect
from FurnitureApp.models import Productclass,Categoryclass
from WebApp.models import Contactclass,Signinclass,Cartclass,checkoutclass
from django.contrib import messages

# Create your views here.

def homepage(request):
    cattt=Categoryclass.objects.all()
    data=Cartclass.objects.filter(username=request.session['name'])
    x=data.count()
    return render(request,"home.html",{'cattt':cattt,'x':x})

def addwebproducts(request):
    productz=Productclass.objects.all()
    data=Cartclass.objects.filter(username=request.session['name'])
    x=data.count()
    return render(request,"webproducts.html",{'productz':productz,'x':x})

def webcontact(request):
    data=Cartclass.objects.filter(username=request.session['name'])
    x=data.count()
    return render(request,"contact.html",{'x':x})   

def savecontact(request):
    if request.method=="POST":
        a=request.POST.get('firstname') 
        b=request.POST.get('lastname')
        c=request.POST.get('contact')
        d=request.POST.get('email')
        e=request.POST.get('message')
        obj=Contactclass(firstname=a,lastname=b,contact=c,email=d,message=e)
        obj.save()
        return redirect(webcontact)

def productsfiltered(request,cat_name):
    productz=Productclass.objects.filter(productcategory=cat_name)
    return render(request,"productsfiltered.html",{'productz':productz})

def singleproduct(request,pro_id):
    data=Productclass.objects.get(id=pro_id)
    return render(request,"singleproduct.html",{'data':data})


def signup(request):
    return render(request,"signup.html")

def signin(request):
    return render(request,"signin.html")

def saveuser(request):
    a=request.POST.get('name')
    b=request.POST.get('contact')
    c=request.POST.get('email')
    d=request.POST.get('pass')  
    e=request.POST.get('re_pass')
    obj=Signinclass(name=a,contact=b,email=c,password=d,repeat=e)
    if Signinclass.objects.filter(name=a).exists():
        messages.warning(request,"Username already exists")
        return redirect(signup)
    if Signinclass.objects.filter(email=c).exists():
        messages.warning(request,"Email address already exists")
        return redirect(signup)
    obj.save()
    return redirect(signup)


def userlogin(request):
    if request.method=="POST":
        u_name=request.POST.get('your_name')
        pswd=request.POST.get('your_pass')
        if Signinclass.objects.filter(name=u_name,password=pswd).exists():
            request.session['name']=u_name
            request.session['password']=pswd
            messages.success(request,"Welcome")
            return redirect(homepage)
        else:
            messages.error(request,"Incorrect Password")
            return redirect(signin)
    else:
        messages.error(request,"Incorrect Username or Password")
        return redirect(signin)    
    

def userlogout(request):
    del request.session['name']
    del request.session['password']
    return redirect(signin)   


def savecart(request):
    if request.method=="POST":
        A=request.POST.get('quantity')
        B=request.POST.get('price')
        C=request.POST.get('totalprice')
        D=request.POST.get('username')
        E=request.POST.get('productname')
        obj=Cartclass(quantity=A,price=B,totalprice=C,username=D,productname=E)
        obj.save()
        return redirect(homepage)

def cart(request):
    
    data=Cartclass.objects.filter(username=request.session['name'])
    x = data.count()
    
    subtotal=0
    shipping_amount=0
    total_amount=0
    for i in data:
        subtotal = subtotal + i.totalprice
        if subtotal>50000:
            shipping_amount = 100
        else:
            shipping_amount = 250  
        total_amount = subtotal + shipping_amount    
    return render(request,"cart.html",{'data':data,'subtotal':subtotal,'shipping_amount':shipping_amount,'total_amount': total_amount ,'x':x})


def delete_Cart(request,del_id):
    x=Cartclass.objects.filter(id=del_id)
    x.delete()
    return redirect(cart)

def checkout(request):
    data=Cartclass.objects.filter(username=request.session['name'])
    subtotal=0
    shipping_amount=0
    total_amount=0
    for i in data:
        subtotal = subtotal + i.totalprice
        if subtotal>50000:
            shipping_amount = 100
        else:
            shipping_amount = 250  
        total_amount = subtotal + shipping_amount    
    return render(request,"checkout.html",{'data':data,'subtotal':subtotal,'shipping_amount':shipping_amount,'total_amount': total_amount })

def savecheckout(request):
    if request.method == "POST":
        a=request.POST.get('firstname')
        c=request.POST.get('email')
        d=request.POST.get('place')
        e=request.POST.get('address')
        f=request.POST.get('pincode')
        g=request.POST.get('mobile')
        h=request.POST.get('total')
        i=request.POST.get('message')
        obj=checkoutclass(firstname=a,email=c,place=d,address=e,pincode=f,mobile=g,total=h,message=i)
        obj.save()
        return redirect(payment)
    
def payment(requet):

    # To retrieve the data from Cartclass with the specified ID
    customer = Cartclass.objects.order_by('-id').first()

    #To get the payment amount of specified customer
    payy=customer.totalprice

    #Convert the amount into paisa (Smallamount)
    amount = int(payy*100)   

    payy_str = str(amount)

    for i in payy_str:
        print(i)

    # if requet.method=="POST":
             
    return render(requet,"payment.html")
