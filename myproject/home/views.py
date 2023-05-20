from django.shortcuts import render
from django.http import HttpResponse
from home.models import Departments,Doctors
from home.forms import BookingForm

# Create your views here.

def index(request):
    return render(request,'index.html')

def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=BookingForm()
    return render(request,'booking.html',{'form':form})

def doctors(request):
    doc=Doctors.objects.all()
    return render(request,'doctors.html',{'data':doc})

def department(request):
    dep=Departments.objects.all()
    return render(request,'department.html',{'data':dep})
