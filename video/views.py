from django.shortcuts import render,redirect,HttpResponse
from .forms import VideoForm
from .models import Video,User,Classification
from User.views import islogin
# Create your views here.

def vupload(request):
    if islogin(request) == False:
        return redirect('/login')
    userid = request.session.get('UserID', None)
    user = User.objects.filter(User_ID=userid).first()
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        tuserid=request.session.get('UserID', None)
        tuser=User.objects.filter(User_ID=tuserid).first()
        if form.is_valid():
            tmodel = Video()
            tmodel.Title = request.POST.get('Title')
            tmodel.Content = request.POST.get('Content')
            tCcode = request.POST.get('Classification')
            tClassification=Classification.objects.filter(Ccode=tCcode).first()
            tmodel.Classification = tClassification
            tmodel.User = tuser
            tmodel.VideoFile = request.FILES.get('VideoFile')
            tmodel.CoverFile = request.FILES.get('CoverFile')
            tmodel.save()
        else:
            print("wrong")
        return redirect('/vupload/')
    else:
        if not (request.session.get('is_login', None) == True):
            return redirect('/s')
        form = VideoForm()
        return render(request,"upload.html",{'form':form,
                                             'user':user})
    

def vmodify(request,dvcode):
    if islogin(request) == False:
        return redirect('/login')
    userid = request.session.get('UserID', None)
    user = User.objects.filter(User_ID=userid).first()
    tvideo=Video.objects.filter(DVcode=dvcode).first()
    if tvideo is None:
        return render(request,"wrong/NosuchFile.html")
    if request.method == 'POST':
        print('herep')
        if request.POST.get('delete') == 'yes':
            print('here')
            tvideo.delete()
            return render(request,"wrong/NosuchFile.html")
        form = VideoForm(instance=tvideo, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        
    if request.method == 'GET':
        form = VideoForm(instance=tvideo)
    return render(request,"modify.html",{'form':form,
                                         'user':user})

def vplay(request,dvcode):
    tvideo=Video.objects.filter(DVcode=dvcode).first()
    if request.method == 'GET':
        return render(request,"play.html",{
            'video':tvideo
        })