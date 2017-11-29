
import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from . forms import *
from . models import *


from rest_framework import viewsets
from osat.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = alumni.objects.all()
    serializer_class = UserSerializer



def index(request):
    dn=datetime.datetime.now()
    cont_dict={'notif' : notif.objects.all().order_by('-timestamp')[:2],'dn':dn}
    return render(request, "osat/index.html", cont_dict)


def about(request):
    return render(request, "osat/about.html")

def chasing_infinity(request):
    return render(request, "osat/chasing_infinity.html")

def a_registration(request):
    paid = ['augustinetharakan12@gmail.com','test@gmail.com','1']
    if request.method == 'POST':
        form1 = detailsform(request.POST)
        form2 = view_events_form(request.POST)
        if 'a_registration' in request.POST:
            if form1.data['email'] in paid :
                a = form1.save(commit=False)
                form1.save()
                return render(request,'osat/submit.html', {'a':a})
            else:
                return render(request, 'osat/a_registration.html',{'view_events_form': view_events_form, 'detailsform': detailsform(), 'pay': 0,'notpaid': 1})
        elif 'pay' in request.POST:
            if form2.data['email'] in paid :
                b=alumni.objects.all().values_list('email',flat='True')
                if form2.data['email'] in b:
                    return render(request,'osat/a_registration.html',{'view_events_form':view_events_form,'detailsform': detailsform(),'pay':1,'notpaid':0,'reg':1})
                else:
                    return render(request, 'osat/a_registration.html',{'view_events_form': view_events_form, 'detailsform': detailsform(), 'pay': 1,'notpaid': 0,'reg':0})
            else :
                return render(request, 'osat/a_registration.html',{'view_events_form': view_events_form, 'detailsform': detailsform(), 'pay': 0,'notpaid':1})
        else:
            return HttpResponse('Form invalid')
    else:
        return render(request, "osat/a_registration.html", {'view_events_form':view_events_form,'detailsform': detailsform(),'pay':0,'notpaid':0})


def h_registration(request):
    if request.method == 'POST':
        form = no_attending_form(request.POST)
        obj2 = alumnievent.objects.filter(email=form.data['email'])
        mail = alumnievent.objects.all().values_list('email', flat='true')
        if form.is_valid() and form.data['email'] in mail :
            return render(request,'osat/view_events.html', {'view_events_form':view_events_form,'suc':1,'obj2':obj2,'email1':0})
        else:
            return render(request, 'osat/view_events.html', {'view_events_form':view_events_form,'suc': 0, 'obj2': obj2,'email1':1})
    else:
        return render(request,"osat/view_events.html",{'view_events_form':view_events_form,'suc':0,'email1':0})
def e_registration(request):
    return render(request,"osat/e_registration.html")
def c_us(request):
    return render(request,"osat/c_us.html")

def h_registration(request):
    if request.method == 'POST':
        form = no_attending_form(request.POST)
        mail = alumni.objects.all().values_list('email', flat='true')
        if form.is_valid() and form.data['email'] in mail :
            a=alumni.objects.filter(email=form.data['email'])
            a.update(no_attending=form.data['no_attending'])
            return render(request,'osat/h_registration.html', {'no_attending_form':no_attending_form,'suc':1,'email1':0})
        else:
            return render(request, 'osat/h_registration.html', {'no_attending_form':no_attending_form,'suc': 0,'email1':1})
    else:
        return render(request,"osat/h_registration.html",{'no_attending_form':no_attending_form,'suc':0,'email1':0})
def e_registration(request):
    return render(request,"osat/e_registration.html")
def c_us(request):
    return render(request,"osat/c_us.html")



def notific(request):
    dn = datetime.datetime.now()
    cont_dict2 = {'notif': notif.objects.all().order_by('-timestamp'), 'dn': dn}
    return render(request, "osat/notifications.html", cont_dict2)



def example(request):
    return JsonResponse({"data": "hello world"})




def ec_registration(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ec_form(request.POST)
        # check whether it's valid:
        pass1=0
        event1=0
        email1=0
        ev1=ec.objects.all().values_list('event',flat='true')
        em1=alumni.objects.all().values_list('email',flat='true')
        if form.is_valid():
            if form.data['password1'] != form.data['password2'] or form.data['event'] in ev1 or form.data['email'] not in em1:
                if form.data['password1'] != form.data['password2'] :
                    pass1=1
                if form.data['event'] in ev1:
                    event1=1
                if form.data['email'] not in em1:
                    email1=1
                return render(request, 'osat/ec_registrationpassmatch.html', {'ec_form': ec_form(),'pass1':pass1,'event1':event1,'email1':email1})
            else:
                a=form.save(commit=False)
                form.save()
                print ("hello")
                return render(request, 'osat/submit.html', {'a': a})
        else:
            return HttpResponse('Form invalid')

            # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, "osat/ec_registration.html", {'ec_form': ec_form()})


def er_registration(request):
    a=ec
    a=a.objects.all()
    return render(request,"osat/er_registration.html",{'a':a})

def el_registration(request):
    if request.method == 'POST':
        form = ec_login_form(request.POST)
        if form.is_valid():
            if form.data['password'] in ec.objects.filter(email=form.data['email']).values_list('password1',flat='true'):
                return render(request, "osat/el_registration.html", {'ec_login_form': ec_login_form(), 'pass1': 0,'suc':1,'obj1':alumni.objects.all(),'obj2':alumnievent.objects.all(),'event':ec.objects.filter(email=form.data['email']).values_list('event',flat='true')})
            else:
                return render(request, "osat/el_registration.html", {'ec_login_form': ec_login_form(), 'pass1': 1,'suc':0,'obj1':alumni.objects.all(),'obj2':alumnievent.objects.all(),'event':ec.objects.filter(email=form.data['email']).values_list('event',flat='true')})
    else:
        return render(request,"osat/el_registration.html",{'ec_login_form':ec_login_form(),'pass1':0,'suc':0,'obj1':alumni.objects.all(),'event':0})
def el_registrationpassmatch(request):
        return render(request,"osat/ec_registrationpassmatch.html")

def er_registration2(request, x):
    al=alumni.objects.all().values_list('email',flat='true')
    if request.method == 'POST':
        form = alumnievent_form(request.POST)
        if form.is_valid():
            if form.data['email'] not in al:
                return render(request, "osat/ers_registration.html",{'alumnievent_form': alumnievent_form, 'email1': 1,'suc':0})
            else:
                a=form.save(commit=False)
                a.event=x
                a.save()
                #i=alumni.objects.filter(email=form.data['email'])
                #i.update(event=x)
                return render(request, "osat/ers_registration.html",{'alumnievent_form': alumnievent_form, 'email1': 0,'suc':1})
    else:
        return render(request, "osat/ers_registration.html",{'alumnievent_form':alumnievent_form,'email1':0,'suc':0})

def el_registration3(request):
    if request.method == 'POST':
        form = view_events_form(request.POST)
        obj2 = alumnievent.objects.filter(email=form.data['email'])
        mail = alumnievent.objects.all().values_list('email', flat='true')
        if form.is_valid() and form.data['email'] in mail :
            return render(request,'osat/view_events.html', {'view_events_form':view_events_form,'suc':1,'obj2':obj2,'email1':0})
        else:
            return render(request, 'osat/view_events.html', {'view_events_form':view_events_form,'suc': 0, 'obj2': obj2,'email1':1})
    else:
        return render(request,"osat/view_events.html",{'view_events_form':view_events_form,'suc':0,'email1':0})

def admin2(request):
    a=alumni
    sum_of_alumni=0
    sum_of_attending=0
    a=a.objects.all().order_by('year_pass')
    j=teachers
    j=j.objects.all()
    for i in a:
        sum_of_alumni=sum_of_alumni+1
        sum_of_attending=sum_of_attending+i.no_attending
    id="osatadmin"
    passw="osat12345"
    if request.method=='POST':
        form = ec_login_form(request.POST)
        if form.is_valid() and form.data['email'] == id and form.data['password'] == passw:
            return render(request,'osat/admin2.html',{'ec_login_form':ec_login_form ,'suc':1,'a':a,'sum_of_alumni':sum_of_alumni,'sum_of_attending':sum_of_attending,'j':j})
        else:
            return render(request, 'osat/admin2.html', {'ec_login_form': ec_login_form, 'suc': 0,'a':a,'sum_of_alumni':sum_of_alumni,'sum_of_attending':sum_of_attending,'j':j})
    else:
        return render(request,"osat/admin2.html",{'ec_login_form':ec_login_form,'suc':0,'a':a,'sum_of_alumni':sum_of_alumni,'sum_of_attending':sum_of_attending,'j':j})


def admin2notification(request):
    a = alumni
    sum_of_alumni = 0
    sum_of_attending = 0
    a = a.objects.all().order_by('year_pass')
    for i in a:
        sum_of_alumni = sum_of_alumni + 1
        sum_of_attending = sum_of_attending + i.no_attending
    id = "osatadmin"
    passw = "osat12345"
    if request.method == 'POST':
        form = notificationsform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'osat/admin2.html',
                          {'ec_login_form': ec_login_form, 'suc': 1, 'a': a, 'sum_of_alumni': sum_of_alumni,
                           'sum_of_attending': sum_of_attending, 'notificationsform': notificationsform})
        else:
            return render(request, 'osat/admin2.html',
                          {'ec_login_form': ec_login_form, 'suc': 1, 'a': a, 'sum_of_alumni': sum_of_alumni,
                           'sum_of_attending': sum_of_attending, 'notificationsform': notificationsform})
    else:
        return render(request,'osat/admin2notification.html',{'notificationsform':notificationsform})


def tickets(request):
    if request.method=='POST':
        form=view_events_form(request.POST)
        mail = alumni.objects.all().values_list('email', flat='true')
        if form.is_valid() and form.data['email'] in mail:
            return render(request,'osat/tickets.html',{'view_events_form':view_events_form,'suc':1,'reg':0})
        else:
            return render(request, 'osat/tickets.html', {'view_events_form':view_events_form,'suc': 0, 'reg': 1})
    else:
        return render(request, 'osat/tickets.html', {'view_events_form':view_events_form,'suc': 0, 'reg': 0})

def chasing_infinity(request):
    return render(request,'osat/chasing_infinity.html')

def t_registration(request):
    if request.method=='POST':
        form=t_registrationform(request.POST)
        if form.is_valid():
            a=form.save(commit="false")
            return render(request,'osat/submit.html',{'a':a})
        else:
            return HttpResponse('form invalid')
    else:
        return render(request,'osat/t_registration.html',{'t_registrationform':t_registrationform})

def registration(request):
    return render(request,'osat/registration.html')