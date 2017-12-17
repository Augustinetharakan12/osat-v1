
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

#people who paid offline
offline_reg = off_registration.objects.all().values_list('email', flat='true')

#people who paid registration fee (RS 500/-)
paid = ['rohithdas20@gmail.com', 'nainakrishnan@gmail.com', 'sumitmammen@gmail.com', 'melvin.moncey@gmail.com', 'mriduldey@gmail.com', 'allen.moncey@gmail.com', 'nishanththarakan@gmail.com', 'dhanyamelam@gmail.com', 'alangodfrey12@gmail.com', 'arunvidyasagar@gmail.com', 'njprince25@hotmail.com', 'sonellamanoj@gmail.com', 'anujgk@gmail.com', 'tharunjohn123@gmail.com', 'georgevt@outlook.com', 'charlesraj88@gmail.com','vivinabraham@gmail.com', 'zaebasgani.zg@gmail.com','elsalex83@gmail.com', 'snehapbijoy@gmail.com', 'swth03@gmail.com']

#combining them both
paid += offline_reg

#total no of people who paid registration fees
paid_no=len(paid)

#homecoming tickets
paid_300=['MOJO7c15005D22253172\tmelvin.moncey@gmail.com', 'MOJO7c15005A22253535\tallen.moncey@gmail.com']
paid_600=['MOJO\trohithdas20@gmail.com']
paid_900=[]
paid_1200=[]
paid_1500=[]
paid_1800=[]
paid_2100=[]

#the main page
def index(request):
    dn=datetime.datetime.now()
    cont_dict={'notif' : notif.objects.all().order_by('-timestamp')[:2],'submit':0,'dn':dn}
    return render(request, "osat/index.html", cont_dict)

#about page
def about(request):
    return render(request, "osat/about.html")

#def chasing_infinity(request):
#    return render(request, "osat/chasing_infinity.html")

#alumni registration
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

#events registration page
def e_registration(request):
    return render(request,"osat/e_registration.html")

#contact us page
#def c_us(request):
#    return render(request,"osat/c_us.html")

#homecoming registration
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

#event registration
def e_registration(request):
    return render(request,"osat/e_registration.html")

#contact us page
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


#all notifications
def notific(request):
    dn = datetime.datetime.now()
    cont_dict2 = {'notif': notif.objects.all().order_by('-timestamp'), 'dn': dn}
    return render(request, "osat/notifications.html", cont_dict2)


#json sample
def example(request):
    return JsonResponse({"data": "hello world"})

#create event
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

#register for an event
def er_registration(request):
    a=ec
    a=a.objects.all()
    return render(request,"osat/er_registration.html",{'a':a})

#event heads login page
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

#register for an event
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

#view registered events by entering the email id
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

#ADMIN
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
        form3 = notificationsform(request.POST)
        if 'adminlogin' in request.POST:
            if form1.is_valid() and form1.data['email'] == id and form1.data['password'] == passw:
                return render(request,'osat/admin2.html',{'ec_login_form':ec_login_form ,'suc':1,'a':a,'sum_of_alumni':sum_of_alumni,'sum_of_attending':sum_of_attending,'j':j,'m':m,'off_reg':off_registration_form,'off_reg_details':off_reg_details,'teachers_registered':teachers_registered,'teacher_homecoming':teacher_homecoming,'paid':paid,'paid_no':paid_no,'notificationsform': notificationsform})
            else:
                return render(request, 'osat/admin2.html', {'ec_login_form': ec_login_form, 'suc': 0,'a':a,'sum_of_alumni':sum_of_alumni,'sum_of_attending':sum_of_attending,'j':j,'j':j,'m':m,'off_reg':off_registration_form,'off_reg_details':off_reg_details,'notificationsform': notificationsform})
        elif 'off_reg' in request.POST:
            if form2.is_valid():
                c=form2.save()
                return render(request, 'osat/admin2.html',{'ec_login_form': ec_login_form, 'suc': 1, 'a': a, 'sum_of_alumni': sum_of_alumni,'sum_of_attending': sum_of_attending, 'j': j, 'm': m, 'off_reg': off_registration_form,'off_reg_details':off_reg_details,'teachers_registered':teachers_registered,'teacher_homecoming':teacher_homecoming,'paid':paid,'paid_no':paid_no,'notificationsform': notificationsform})
        elif 'notification' in request.POST:
            if form3.is_valid():
                form3.save()
                return render(request, 'osat/admin2.html',{'ec_login_form': ec_login_form, 'suc': 1, 'a': a, 'sum_of_alumni': sum_of_alumni,'sum_of_attending': sum_of_attending, 'j': j, 'm': m, 'off_reg': off_registration_form,'off_reg_details': off_reg_details,'teachers_registered':teachers_registered,'teacher_homecoming':teacher_homecoming,'paid':paid,'paid_no':paid_no, 'notificationsform': notificationsform})
            else :
                return HttpResponse('Invalid')
    else:
        return render(request,"osat/admin2.html",{'ec_login_form':ec_login_form,'suc':0,'a':a,'sum_of_alumni':sum_of_alumni,'sum_of_attending':sum_of_attending,'j':j,'j':j,'m':m})

#admin2 notication .. now disabled because it takes you to a new page
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

#Tickets
def tickets(request):
    if request.method=='POST':
        form=tickets_form(request.POST)
        #mail = alumni.objects.all().values_list('email', flat='true')

        unique_code=form.data['code']
        var='\t'
        unique_code=unique_code+var
        unique_code=unique_code+form.data['email']

        if form.is_valid() and unique_code in paid_300 or unique_code in paid_600 or unique_code in paid_900 or unique_code in paid_1200 or unique_code in paid_1500 or unique_code in paid_1800 or unique_code in paid_2100:
            if unique_code in paid_300:
                admit='1'
            elif unique_code in paid_600:
                admit='2'
            elif unique_code in paid_900:
                admit='3'
            elif unique_code in paid_1200:
                admit='4'
            elif unique_code in paid_1500:
                admit='5'
            elif unique_code in paid_1800:
                admit='6'
            elif unique_code in paid_2100:
                admit='7'

            alumni_email=alumni.objects.filter(email=form.data['email']).values_list('email',flat='true')
            alumni_pk=alumni.objects.filter(email=form.data['email']).values_list('pk',flat='true')

            #alumni_admits=alumni.objects.filter(email=form.data['email']).values_list('no_attending',flat='true')

            #url2 = 'C:/Users/THARAKAN/Desktop/ticket.png'
            #url2='/home/django/django_project/osat/static/osat/ticket.png'

            #same for windows and ubundu
            url2='osat/static/osat/ticket.png'

            image = Image.open(url2)

            #for windows normal... for ubundu must download arial.ttf and paste it in the directory
            font = ImageFont.truetype("arial.ttf", 20)
            font2 = ImageFont.truetype("arial.ttf", 30)
            font3 = ImageFont.truetype("arial.ttf", 20)
            #end

            draw = ImageDraw.Draw(image)

            email_image=alumni_email[0]
            pk_image=str(alumni_pk[0])

            draw.text(xy=(40, 185), text="E-mail:"+email_image, fill=(0, 0, 0), font=font)
            draw.text(xy=(660, 178), text=admit, fill=(255, 255, 255), font=font2)
            draw.text(xy=(600, 220), text="Ticket No:"+pk_image, fill=(255, 255, 255), font=font3)

            # image.save('C:\Users\THARAKAN\Desktop\ti2.png', 'JPEG')
            # im.save(file + ".png", "JPEG")

            #for windows
            image.save('osat/static/osat/user_ticket.png')

            #for ubundu server
            #image.save('django_project/static/osat/user_ticket.png')


            #response = HttpResponse(content_type="image/png")
            #image.save(response,"png")
            #return response

            return render(request, 'osat/tickets.html', {'tickets_form': tickets_form, 'suc': 1, 'reg': 0})

            #return render(request,'osat/tickets.html',{'view_events_form':view_events_form,'suc':1,'reg':0})
        else:
            return render(request, 'osat/tickets.html', {'tickets_form':tickets_form,'suc': 0, 'reg': 1})
    else:
        return render(request, 'osat/tickets.html', {'tickets_form':tickets_form,'suc': 0, 'reg': 0})

#powered by chasing infinity
def chasing_infinity(request):
    return render(request,'osat/chasing_infinity.html')

#teachers registration
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

#teachers regitration for homecoming
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

#the main registration page
def registration(request):
    return render(request,'osat/registration.html')

#The main payments page
def payments(request):
    return render(request,'osat/payments.html')

#Page for donations
def donations(request):
    return render(request,'osat/donations.html')