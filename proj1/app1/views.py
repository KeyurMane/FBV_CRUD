from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from .models import Laptop
from .forms import LaptopModelForm
# Create your views here.
def dispview(request):
    obj = Laptop.objects.all()
    temp_nm = 'disp.html'
    context = {'obj':obj}
    return render(request,temp_nm,context)

def createview(request):
    if request.method == 'GET':
        temp_nm = 'create.html'
        form = LaptopModelForm()
        context = {'form':form}
        return render(request,temp_nm,context)
    elif request.method == 'POST':
        form = LaptopModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disp')
        else:
            return HttpResponse('form is invalid')

def updtview(request,id):
    obj = Laptop.objects.get(id=id)
    form = LaptopModelForm(instance=obj)
    if request.method == "POST":
        form = LaptopModelForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('disp')
    temp_nm = 'create.html'
    context = {'form':form}
    return render(request,temp_nm,context)

def delview(request,id):
    obj = Laptop.objects.get(id=id)
    obj.delete()
    return redirect('disp')

