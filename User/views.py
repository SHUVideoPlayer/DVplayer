import datetime

from django.shortcuts import render,HttpResponse,redirect
from .forms import RegisterForm
from User import models
from django.utils import timezone
import pytz

tz = pytz.timezone('Asia/Shanghai')
# Create your views here.
def Register(request):
    RegiForm=RegisterForm()
    if (request.method=="POST") & (request.POST.get('addUser')=='yes'):
        form=RegisterForm(request.POST,request.FILES)
        md1=models.User()
        md1.User_ID=request.POST.get('User_ID')
        md1.NickName=request.POST.get('NickName')
        md1.Password=request.POST.get('Password')
        md1.Email=request.POST.get('Email')
        md1.Phone_number=request.POST.get('Phone_number')
        md1.Profile_photo=request.FILES.get('Profile_photo')
        now_time = timezone.now().astimezone(tz=tz).strftime("%Y-%m-%d %H:%M:%S")
        now = datetime.datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S')
        md1.Register_time=now
        md1.save()
        print(md1.User_ID)
        if form.is_valid():
            if models.User.objects.filter(User_ID=form.Meta.model.User_ID) is not None:
                print("Username has existed")
            #print(NewStu)
            else:
                form.save()
                print('success save')
            #print(request.POST.get('Stu_Department'))


    return render(request,'Register.html',{
                                            'RegisterForm':RegiForm
                                            })