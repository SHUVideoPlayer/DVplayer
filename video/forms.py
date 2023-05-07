from django import forms 
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["Title","Classification","VideoFile","CoverFile",]
        labels = {"Title":"视频标题","Classification":"视频分区","VideoFile":"视频文件","CoverFile":"封面文件"}
