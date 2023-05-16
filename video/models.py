from django.db import models
from django.core import validators
from User.models import User
# Create your models here.

class Classification(models.Model):
    Ccode = models.AutoField(primary_key=True,verbose_name="视频分区号")
    Title = models.CharField(max_length=20,verbose_name="视频分区")
    
    def __str__(self):
        return self.Title
    
    class Meta:
        db_table = "视频分区"

class Video(models.Model):
    DVcode = models.AutoField(primary_key=True,verbose_name="视频号")
    Title = models.CharField(max_length=100,verbose_name="视频名称")
    ReleaseTime = models.DateTimeField(auto_now_add=True,verbose_name="发布时间")
    Viewsnum = models.BigIntegerField(default=0,verbose_name="播放量")
    User = models.ForeignKey(User,on_delete=models.CASCADE,null=True,verbose_name="作者")
    Classification = models.ForeignKey(Classification,on_delete=models.CASCADE,null=True,verbose_name="分区")
    Content = models.CharField(max_length=500,default="该用户很懒，it什么也没有说！",verbose_name="视频简介")
    VideoFile = models.FileField(upload_to="video/",validators=[validators.FileExtensionValidator( ['mp4'] )] ,verbose_name="视频文件")
    CoverFile = models.ImageField(upload_to="cover/",verbose_name="封面文件")
    
    def __str__(self):
        return self.Title
    
    class Meta:
        db_table = "视频"
    
    

