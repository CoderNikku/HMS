from django.shortcuts import render
from HealthCenter.forms import AppointmentForm
from django.http import HttpResponse
# Create your views here.


def view_base(request):
    resp=render(request , 'HealthCenter/base.html')
    return resp

def view_home(request):
    resp=render(request, 'HealthCenter/home.html')
    return resp

def view_about(request):
    resp=render(request, 'HealthCenter/about.html')
    return resp

def view_doctors(request):
    resp=render(request, 'HealthCenter/doctors.html')
    return resp

def view_news(request):
    resp=render(request, 'HealthCenter/news.html')
    return resp

def view_contact(request):
    resp=render(request, 'HealthCenter/contact.html')
    return resp

def view_appointment(request):
    if request.method=='GET':
        frm_unbound=AppointmentForm
        d1={'forms':frm_unbound}
        resp=render(request, 'HealthCenter/appointment.html',context=d1)
        return resp
    elif request.method=='POST':
        frm_bound=AppointmentForm(request.POST)
        if frm_bound.is_valid:
            frm_bound.save()
            resp=HttpResponse("<h1>successfully add data</h>")
            return resp
