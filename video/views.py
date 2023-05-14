from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import VideoForm
from .models import Video,User,Classification
# Create your views here.


    
def vupload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        tuserid=request.session.get('UserID', None)
        tuser=User.objects.filter(User_ID=tuserid).first()
        if form.is_valid():
            tmodel = Video()
            tmodel.Title = request.POST.get('Title')
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
            print("here")
            return redirect('/s')
        
        form = VideoForm()
        return render(request,"upload.html",{'form':form})
    



