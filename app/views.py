from django.shortcuts import render,redirect,get_object_or_404
from app.form import userRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from .models import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

response={}
response['ct']=category.objects.all()
response['p']=product.objects.all()
response['f']=userRegisterForm()


def home(request):
    pro=product.objects.all()
    paginator=Paginator(pro,4)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    response['pro']=page_obj
    return render(request,'home.html',response)

def register(request):
    if request.method=='POST':
        f=userRegisterForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request,'Your accout created successfully')
            return render(request,'register.html',{'f':f})
    f=userRegisterForm()
    return render(request,'register.html',response)

def log(request):
    if request.method=='POST':
        un=request.POST['username']
        psd=request.POST['password']
        user=authenticate(username=un,password=psd)
        if user is not None:
            f1=login(request, user)
            response['f1']=f1
            messages.success(request,'welcome')
            return render(request,'home.html',response)
        else:
            messages.info(request,'user does not exist')
    f1=AuthenticationForm()
    return render(request,'login.html',{'f1':f1})

def cat(request,a):
    c=product.objects.all().filter(category_id=a)
    return render(request,'cat.html',{'c':c})

def cart(request,x):
    response['a']=x
    return render(request,'cart.html',response)

def search(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=product.objects.all().filter(Q(name__contains=query))
    return render(request,'search.html',{'qr':query,'pr':prod})


def cart_details(request,tot=0,count=0,cart_items=None):
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
        ct_items=item.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot +=(i.prodt.price*i.quan)
            count +=i.quan
    except ObjectDoesNotExist:
        pass
    return render(request,'c.html',{'ci':ct_items,'t':tot,'cn':count})

def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id

def add_cart(request, product_id):
    prod=product.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items=item.objects.get(prodt=prod,cart=ct)
        if c_items.quan < c_items.prodt.stock:
            c_items.quan+=1
        c_items.save()
    except item.DoesNotExist:
        c_items=item.objects.create(prodt=prod,quan=1,cart=ct)
        c_items.save()
    return redirect('cart_details')

def min_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(product,id=product_id)
    c_items=item.objects.get(prodt=prod,cart=ct)
    if c_items.quan>1:
        c_items.quan-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cart_details')

def cart_delete(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(product,id=product_id)
    c_items=item.objects.get(prodt=prod,cart=ct)
    c_items.delete()
    return redirect('cart_details')

def pay(request,t):
    return render(request,'payment.html',{'t':t})

