from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from .forms import ProductForm
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def baseview(request):
    template_name='InventoryManagement/base.html'
    context={}
    return render(request,template_name,context)


@login_required(login_url='login')
def submitview(request):
    form = ProductForm()

    if request.method=='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showall')

    template_name='InventoryManagement/submitform.html'
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='login')
def showproductview(request):
    template_name = 'InventoryManagement/showproducts.html'
    all_products = Product.objects.all()
    context = {'all_products':all_products}
    return render(request, template_name, context)

def deleteproductview(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('showall')


def updateproductview(request,id):
    obj = Product.objects.get(id=id)
    form= ProductForm(instance=obj)

    if request.method=='POST':
        form = ProductForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showall')

    template_name='InventoryManagement/submitform.html'
    context = {'form': form}
    return render(request, template_name, context)


def registerview(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    template_name = 'InventoryManagement/registrationform.html'
    context = {'form': form}
    return render(request, template_name, context)


def loginview(request):
    if request.method=='POST':
        U=request.POST.get('u')
        P=request.POST.get('p')

        user=authenticate(username=U,password=P)

        if user is not None:
            login(request,user)
            return redirect('showall')
        else:
            messages.error(request,'Invalid Credentials')

    template_name='InventoryManagement/loginform.html'
    context={}
    return render(request,template_name,context)


def logoutview(request):
    logout(request)
    return redirect('login')






