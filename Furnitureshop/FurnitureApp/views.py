from django.shortcuts import render,redirect
from FurnitureApp.models import Categoryclass,Productclass
from WebApp.models import Contactclass
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def index(request):
    categorynos=Categoryclass.objects.count
    return render(request,"index.html")

def addcategoryfn(request):
    return render(request,"addcategory.html")

def savecategoryfn(request):
    if request.method=="POST":
        a=request.POST.get('categoryname')
        b=request.FILES['picture']
        c=request.POST.get('description')
        obj=Categoryclass(cname=a,cimage=b,cdescription=c)
        obj.save()
        messages.success(request,"Category Saved...!")
        return redirect(addcategoryfn)
    
def displaycategoryfn(request):
    data=Categoryclass.objects.all()
    return render(request,"displaycategory.html",{'data':data})

def editcategoryfn(request,edit_id):
    ed=Categoryclass.objects.get(id=edit_id)
    return render(request,"editcategory.html",{'ed':ed})    

def updatecategoryfn(request,edit_id):
    if request.method=="POST":
        a=request.POST.get('categoryname')
        try:
            b=request.FILES['picture']
            fs=FileSystemStorage()
            file=fs.save(b.name,b)
        except MultiValueDictKeyError:
            file=Categoryclass.objects.get(id=edit_id).cimage    
        c=request.POST.get('description')
        Categoryclass.objects.filter(id=edit_id).update(cname=a,cimage=file,cdescription=c)
        messages.info(request,"Category Updated")
        return redirect(displaycategoryfn)

def deletecategoryfn(request,del_id):
    x=Categoryclass.objects.filter(id=del_id)
    x.delete()
    messages.error(request,"Category Deleted !")
    return redirect(displaycategoryfn)

 
#Product details starts here.....!    


def addproductfn(request):
    dicty=Categoryclass.objects.all()
    return render(request,"addproduct.html",{'dicty':dicty})

def saveproductfn(request):
    if request.method=="POST":
        a=request.POST.get('productcategory')
        b=request.POST.get('productname')
        c=request.POST.get('quantity')
        d=request.POST.get('price')
        e=request.POST.get('description')
        f=request.POST.get('country')
        g=request.POST.get('manufactured')
        h=request.FILES['image1']
        i=request.FILES['image2']
        j=request.FILES['image3']
       
        obj=Productclass(productcategory=a,productname=b,quantity=c,price=d,description=e,countryoforigin=f,manufacturedby=g,productimage1=h,productimage2=i,productimage3=j)
        obj.save()
        messages.success(request,"Category Saved")
        return redirect(addproductfn)

def displayproductfn(request):
    prod=Productclass.objects.all()
    return render(request,"displayproduct.html",{'prod':prod})

def editproductfn(request,editprod_id):
    dat=Categoryclass.objects.all()
    edits=Productclass.objects.get(id=editprod_id)
    return render(request,"editproduct.html",{'edits':edits,'dat':dat})

def updateproductfn(request,editprod_id):
    if request.method=="POST":
        a=request.POST.get('productcategory')
        b=request.POST.get('productname')
        c=request.POST.get('quantity')
        d=request.POST.get('price')
        e=request.POST.get('description')
        f=request.POST.get('country')
        g=request.POST.get('manufactured')
        try:
            h=request.FILES['image1']
            fs=FileSystemStorage()
            file=fs.save(h.name,h)
        except MultiValueDictKeyError:
            file=Productclass.objects.get(id=editprod_id).productimage1
        try:
            i=request.FILES['image2']
            fs=FileSystemStorage()
            files=fs.save(i.name,i)
        except MultiValueDictKeyError:
            files=Productclass.objects.get(id=editprod_id).productimage2 
        try:
            j=request.FILES['image3']
            fs=FileSystemStorage()
            filess=fs.save(j.name,j)
        except MultiValueDictKeyError:
            filess=Productclass.objects.get(id=editprod_id).productimage3  
        Productclass.objects.filter(id=editprod_id).update(productcategory=a,productname=b,quantity=c,price=d,description=e,countryoforigin=f,manufacturedby=g,productimage1=file,productimage2=files,productimage3=filess) 
        messages.info(request,"Product Updated")
        return redirect(displayproductfn)

def deleteproductfn(request,dell_id):
    y=Productclass.objects.get(id=dell_id)
    y.delete()
    messages.error(request,"Product Deleted !")
    return redirect(displayproductfn)        


def adminpage(request):
    return render(request,"admin_login.html")

def adminlogin(request):
    if request.method=="POST":
        u_name=request.POST.get('username')
        pswd=request.POST.get('pass')
        if User.objects.filter(username__contains=u_name).exists():
            usernamedetials=authenticate(username=u_name,password=pswd)
            if usernamedetials is not None:
                login(request,usernamedetials)
                request.session['username']=u_name
                request.session['password']=pswd 
                messages.success(request,"Welcome")
                return redirect(index)
            else:
                messages.error(request,"Incorrect Password")
                return redirect(adminpage)
        else:
            messages.error(request,"Invalid username or Password")
            return redirect(adminpage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminpage)           

def displaycontact(request):
    displaycontact=Contactclass.objects.all()
    return render(request,"displaycontact.html",{'displaycontact':displaycontact})
    