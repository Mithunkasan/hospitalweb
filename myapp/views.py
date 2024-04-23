from django.shortcuts import render

from myapp.form import bookingform
from myapp.models import Booking, Doctors, Departments


def homepage(request):
    return render(request, 'home.html')

def displayfunction(request):
    s1=Doctors.objects.all()

    dist1={'doct':s1}
    return render(request,'doctors.html',dist1)

def displayfunction2(request):
    s2 = Departments.objects.all()
    dict1={'depart':s2}
    return render(request,'department.html',dict1)

def Loadform(request):
    form1=bookingform()
    dict2={'myform':form1}
    if request.method == 'POST':
        form1=bookingform(request.POST)
        if form1.is_valid():
            form1.save()

    return render(request, 'bookingform.html',dict2)

def contactpage(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')