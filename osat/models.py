import datetime
from django.db import models

class alumni(models.Model):
    fname=models.CharField(max_length=200,null=True)
    lname=models.CharField(max_length=200,null=True)
    year_pass=models.IntegerField(null=True)
    id = models.IntegerField(primary_key=True)
    #student=models.CharField(max_length=2,null=True)#y or N
    #inst_name=models.CharField(max_length=200,null=True)
    phno=models.CharField(max_length=15,null=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    #dob=models.DateField
    # address info
    #a_street = models.CharField(max_length=200,null=True)
    #a_city = models.CharField(max_length=200,null=True)
    #a_state = models.CharField(max_length=200,null=True)
    #a_country = models.CharField(max_length=200,null=True)
    #a_pin = models.CharField(max_length=50,null=True)
    #event info
    #event=models.CharField(max_length=30,default='none')

    no_attending=models.IntegerField(default=0)

    def __str__(self):
        return self.fname+' '+ self.lname
#teachers registration

class teachers(models.Model):
    fname = models.CharField(max_length=200, null=True)
    lname = models.CharField(max_length=200, null=True)
    subject = models.CharField(max_length=200, null=True)
    ph_no = models.CharField(max_length=200, null=True)
    e_mail = models.CharField(max_length=200, null=True)
    yearin = models.IntegerField(null=True)
    yearout = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.fname+' '+ self.lname

class notif(models.Model):
    fname=models.CharField(max_length=510,null=True)
    title=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=500,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title+' '+ self.fname

class ec(models.Model):
    email=models.CharField(max_length=50,null=True)
    password1=models.CharField(max_length=50,null=True)
    password2=models.CharField(max_length=50,null=True)
    event=models.CharField(max_length=50,null=True)
    def __str__(self):
        return ' '+ self.email+' '+self.event
class ec_login(models.Model):
    email=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)
    def __str__(self):
        return ' '+ self.email+' '+self.password
class alumnievent(models.Model):
    email=models.CharField(max_length=50,null=True)
    event=models.CharField(max_length=50,default='None')
    #def event(self,event):

class view_events(models.Model):
    email = models.CharField(max_length=50, null=True)

class homecoming(models.Model):
    email=models.CharField(max_length=50,null=True)
    no_attending=models.IntegerField(null=True)

class c_us_messge(models.Model):
    name= models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50, null=True)
    message=models.CharField(max_length=200,null=True)