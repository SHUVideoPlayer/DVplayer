import datetime

from django.shortcuts import render,HttpResponse,redirect
from .forms import RegisterForm,EditProfileForm
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
        md1.Background_photo=request.FILES.get('Profile_photo')
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

def test(request):
    return render(request, 'index.html')


def UserPage(request):
    islogin(request)
    userid=request.session.get('UserID', None)
    user=models.User.objects.filter(User_ID=userid).first()
    print(user.Email)
    print(user.Profile_photo.url)
    return render(request,'author.html',{'user':user})

def islogin(request):
    if not (request.session.get('is_login', None) == True):
        return(request,'signin.html')
def signin(request):
    islogin(request)
    if (request.method == "POST"):
        Useremail=request.POST.get('email')
        Userpassword=request.POST.get('password')
        try:
            user=models.User.objects.filter(Email=Useremail).first()
            if user.Password == Userpassword:
                request.session['is_login']=True
                request.session['UserID']=user.User_ID
                print('true')
                return UserPage(request)
        except:
                print('无此邮箱')
    return render(request, 'signin.html')

def profile(request):
    islogin(request)
    userid = request.session.get('UserID', None)
    user = models.User.objects.filter(User_ID=userid).first()
    if request.method == 'POST':
        form = EditProfileForm(instance=user,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
    if request.method == 'GET':
        form = EditProfileForm(instance=user)
    return render(request, 'profile.html',{'user':user,
                                           'form':form
                                           })

def password(request):
    islogin(request)
    userid = request.session.get('UserID', None)
    user = models.User.objects.filter(User_ID=userid).first()
    if request.method == 'POST':
        pwd=request.POST.get('pswd')
        user.Password=pwd
        user.save()

    return render(request, 'password.html',{'user':user}
                  )

def imgcenter(request):
    islogin(request)
    userid = request.session.get('UserID', None)
    user = models.User.objects.filter(User_ID=userid).first()


    return render(request, 'imgcenter.html',{'user':user}
                  )