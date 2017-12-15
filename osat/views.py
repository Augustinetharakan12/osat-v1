
import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from PIL import Image, ImageDraw, ImageFont

#import mime


#json
import json
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from collections import namedtuple

from . forms import *
from . models import *


from rest_framework import viewsets
from osat.serializers import UserSerializer

from django.contrib.staticfiles.templatetags.staticfiles import static


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = alumni.objects.all()
    serializer_class = UserSerializer

#json
def ind(request):
    if request.method=='POST':
        rec=json.loads(request.body)
        x=namedtuple("object1",rec.keys())(*rec.values())
        d=alumni.objects.create()
        d.fname=x.fname
        d.lname=x.lname
        d.email=x.email
        d.phno=x.phone
        d.year_pass=2016
        d.save()
        return StreamingHttpResponse(str(rec))
    return StreamingHttpResponse('was GET')

#people who paid
offline_reg = off_registration.objects.all().values_list('email', flat='true')
paid = ['rohithdas20@gmail.com', 'nainakrishnan@gmail.com', 'sumitmammen@gmail.com', 'melvin.moncey@gmail.com', 'mriduldey@gmail.com', 'allen.moncey@gmail.com', 'nishanththarakan@gmail.com', 'dhanyamelam@gmail.com', 'alangodfrey12@gmail.com', 'arunvidyasagar@gmail.com', 'njprince25@hotmail.com', 'sonellamanoj@gmail.com', 'anujgk@gmail.com', 'tharunjohn123@gmail.com', 'georgevt@outlook.com', 'charlesraj88@gmail.com']
paid += offline_reg
paid_no=len(paid)



def index(request):
    dn=datetime.datetime.now()
    cont_dict={'notif' : notif.objects.all().order_by('-timestamp')[:2],'submit':0,'dn':dn}
    return render(request, "osat/index.html", cont_dict)


def about(request):
    return render(request, "osat/about.html")

def chasing_infinity(request):
    return render(request, "osat/chasing_infinity.html")

def a_registration(request):
    paid=[]
    reg_e=alumni.objects.all().values_list('email',flat='true')
    if request.method == 'POST':
        form1 = detailsform(request.POST)
        form2 = view_events_form(request.POST)
        if 'a_registration' in request.POST:
            if 1:#form1.data['email'] in paid :
                if form1.data['email'] not in reg_e:
                    a = form1.save(commit=False)
                    form1.save()
                    #return render(request,'osat/index.html', {'name':a,'submit':1})
                    return render(request,'osat/payments.html', {'name':a,'submit':1})
                else :
                    return render(request, "osat/a_registration.html",{'view_events_form': view_events_form, 'detailsform': detailsform(), 'pay': 1,'notpaid': 0, 'reg': 0,'reg_e':1})
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
        return render(request, "osat/a_registration.html", {'view_events_form':view_events_form,'detailsform': detailsform(),'pay':1,'notpaid':0,'reg':0,'reg_e':0})


def e_registration(request):
    return render(request,"osat/e_registration.html")

def c_us(request):
    return render(request,"osat/c_us.html")

def h_registration(request):
    if request.method == 'POST':
        form = no_attending_form(request.POST)
        mail = alumni.objects.all().values_list('email', flat='true')
        if form.is_valid():
            if form.data['email'] not in paid:
                return render(request, 'osat/h_registration.html',{'no_attending_form': no_attending_form, 'suc': 0, 'email1': 2, 'noattend': 0})
            elif form.data['email'] in mail :
                a=alumni.objects.filter(email=form.data['email'])
                a.update(no_attending=form.data['no_attending'])
                no=int(form.data['no_attending'])
                cost=no*300
                if int(form.data['no_attending']) < 8:
                    return render(request, "osat/h_registration.html",{'no_attending_form': no_attending_form, 'suc': 1, 'email1': 0,'cost':cost})
                else:
                    return render(request, 'osat/h_registration.html',{'no_attending_form': no_attending_form, 'suc': 0, 'email1': 0,'noattend':1})
            else:
                return render(request, 'osat/h_registration.html',{'no_attending_form': no_attending_form, 'suc': 0, 'email1': 1, 'noattend': 0})
            #return render(request,'osat/h_registration.html', {'no_attending_form':no_attending_form,'suc':1,'email1':0})
        else:
            return render(request, 'osat/h_registration.html', {'no_attending_form':no_attending_form,'suc': 0,'email1':1,'noattend':0})
    else:
        return render(request,"osat/h_registration.html",{'no_attending_form':no_attending_form,'suc':0,'email1':0,'noattend':0})
def e_registration(request):
    return render(request,"osat/e_registration.html")


def c_us(request):
    if(request.method == 'POST'):
        form=c_us_message_form(request.POST)
        if form.is_valid :
            a=form.save(commit=False)
            a.save()
            return render(request,'osat/c_us.html',{'form':c_us_message_form,'v':1})
        else:
            return HttpResponse('Form invalid')
    else :
        return render(request,"osat/c_us.html",{'form':c_us_message_form,'v':0})



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
                return render(request, 'osat/index.html', {'name':a,'submit':1,'notif' : notif.objects.all().order_by('-timestamp')[:2],'dn':datetime.datetime.now()})
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

    m=c_us_messge
    m=m.objects.all()

    off_reg_details=off_registration
    off_reg_details=off_registration.objects.all()

    teacher_homecoming=0
    teachers_registered=0
    for i in j:
        teachers_registered+=1
        teacher_homecoming+=i.no_attending
    for i in a:
        sum_of_alumni=sum_of_alumni+1
        sum_of_attending=sum_of_attending+i.no_attending
    id="osatadmin"
    passw="osat12345"
    if request.method=='POST':
        form1 = ec_login_form(request.POST)
        form2 = off_registration_form(request.POST)
        if 'adminlogin' in request.POST:
            if form1.is_valid() and form1.data['email'] == id and form1.data['password'] == passw:
                return render(request,'osat/admin2.html',{'ec_login_form':ec_login_form ,'suc':1,'a':a,'sum_of_alumni':sum_of_alumni,'sum_of_attending':sum_of_attending,'j':j,'m':m,'off_reg':off_registration_form,'off_reg_details':off_reg_details,'teachers_registered':teachers_registered,'teacher_homecoming':teacher_homecoming,'paid':paid,'paid_no':paid_no})
            else:
                return render(request, 'osat/admin2.html', {'ec_login_form': ec_login_form, 'suc': 0,'a':a,'sum_of_alumni':sum_of_alumni,'sum_of_attending':sum_of_attending,'j':j,'j':j,'m':m,'off_reg':off_registration_form,'off_reg_details':off_reg_details})
        elif 'off_reg' in request.POST:
                if form2.is_valid():
                    c=form2.save()
                    return render(request, 'osat/admin2.html',
                                  {'ec_login_form': ec_login_form, 'suc': 1, 'a': a, 'sum_of_alumni': sum_of_alumni,
                                   'sum_of_attending': sum_of_attending, 'j': j, 'm': m, 'off_reg': off_registration_form,'off_reg_details':off_reg_details})
    else:
        return render(request,"osat/admin2.html",{'ec_login_form':ec_login_form,'suc':0,'a':a,'sum_of_alumni':sum_of_alumni,'sum_of_attending':sum_of_attending,'j':j,'j':j,'m':m})


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
                           'sum_of_attending': sum_of_attending, 'notificationsform': notificationsform,})
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
            alumni_email=alumni.objects.filter(email=form.data['email']).values_list('email',flat='true')
            alumni_pk=alumni.objects.filter(email=form.data['email']).values_list('pk',flat='true')

            #alumni_admits=alumni.objects.filter(email=form.data['email']).values_list('no_attending',flat='true')

            #url1 = 'C:/Users/THARAKAN/Desktop/ticket.png'
            #url2='/home/django/django_project/osat/static/osat/ticket.png'
            url2='ticket.png'

            image = Image.open(url2)

            #for windows
            #font = ImageFont.truetype("arial.ttf", 20)
            #font2 = ImageFont.truetype("arial.ttf", 30)
            #font3 = ImageFont.truetype("arial.ttf", 20)
            #end

            #for ubuntu
            font = ImageFont.truetype("arial.ttf", 20)
            font2 = ImageFont.truetype("arial.ttf", 30)
            font3 = ImageFont.truetype("arial.ttf", 20)
            #end

            draw = ImageDraw.Draw(image)

            email_image=alumni_email[0]
            pk_image=str(alumni_pk[0])

            draw.text(xy=(40, 185), text="E-mail:"+email_image, fill=(0, 0, 0), font=font)
            draw.text(xy=(660, 178), text="1", fill=(255, 255, 255), font=font2)
            draw.text(xy=(600, 220), text="Ticket No:"+pk_image, fill=(255, 255, 255), font=font3)

            # image.save('C:\Users\THARAKAN\Desktop\ti2.png', 'JPEG')
            # im.save(file + ".png", "JPEG")
            # end image of ticket

            response = HttpResponse(content_type="image/png")
            image.save(response,"png")
            return response

            #return render(request,'osat/tickets.html',{'view_events_form':view_events_form,'suc':1,'reg':0})
        else:
            return render(request, 'osat/tickets.html', {'view_events_form':view_events_form,'suc': 0, 'reg': 1})
    else:
        return render(request, 'osat/tickets.html', {'view_events_form':view_events_form,'suc': 0, 'reg': 0})

def chasing_infinity(request):
    return render(request,'osat/chasing_infinity.html')

def t_registration(request):
    if request.method=='POST':
        form=t_registrationform(request.POST)
        form2=view_events_form(request.POST)
        registered = teachers.objects.all().values_list('e_mail', flat='true')
        if 'teacher_registation' in request.POST:
            if form.is_valid():
                if form.data['e_mail'] in registered :
                    return render(request, 'osat/t_registration.html',{'t_registration_homecomingform':view_events_form,'t_registrationform': t_registrationform, 'submit': 0,'email':1})
                else:

                    a=form.save(commit="false")
                    teacher_data=teachers.objects.filter(e_mail=form.data['e_mail'])
                    teacher_details=teachers.objects.filter(e_mail=form.data['e_mail'])
                    return render(request, 'osat/index.html', {'teacher_details': teacher_details, 'submit': 2,'notif': notif.objects.all().order_by('-timestamp')[:2],'dn': datetime.datetime.now()})
                    #return render(request,'osat/t_registration.html',{'t_registration_homecomingform':view_events_form,'t_registrationform':t_registrationform,'teacher_data':teacher_data,'submit':1})
                    #return render(request,'osat/index.html',{'name':a,'submit':1})
            else:
                return HttpResponse('form invalid')
        elif 'teacher_homecoming' in request.POST:
            if form2.is_valid:
                if form2.data['email'] in registered:
                    teacher_data = teachers.objects.filter(e_mail=form2.data['email'])
                    return render(request, 'osat/t_registration.html',{'t_registration_homecomingform': view_events_form,'t_registrationform': t_registrationform, 'teacher_data': teacher_data, 'submit': 1})
                else :
                    return render(request, 'osat/t_registration.html',{'t_registration_homecomingform': view_events_form,'t_registrationform': t_registrationform, 'submit': 0,'submit2':1})
    else:
        return render(request,'osat/t_registration.html',{'t_registration_homecomingform':view_events_form,'t_registrationform':t_registrationform,'submit':0,'submit2':0})

def t_registration_homecoming(request, email):
    teacher_details=teachers.objects.filter(pk=email)
    if request.method=='POST':
        form = t_registration_homecomingform(request.POST)
        if form.is_valid():
            teacher_details.update(no_attending=form.data['no_attending'])
            return render(request,'osat/index.html',{'teacher_details':teacher_details,'submit':2,'notif' : notif.objects.all().order_by('-timestamp')[:2],'dn':datetime.datetime.now()})
            #render(request, 'osat/t_registration_homecoming.html',{'form': t_registration_homecomingform, 'email': email, 'teacher_details': teacher_details})
    else:
        return render(request,'osat/t_registration_homecoming.html',{'form':t_registration_homecomingform,'email':email,'teacher_details':teacher_details})

def registration(request):
    return render(request,'osat/registration.html')

def payments(request):
    return render(request,'osat/payments.html')

def donations(request):
    return render(request,'osat/donations.html')