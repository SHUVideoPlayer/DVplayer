from django.shortcuts import render,redirect
from .forms import VideoForm
from .models import Video
# Create your views here.


def vupload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print("wrong")
        return redirect('vupload/')
    else:
        form = VideoForm()
        print("hhh")
        return render(request,"upload.html",{'form':form})
    



