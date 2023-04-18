from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class User(models.Model):
    User_ID = models.CharField(max_length=20,primary_key=True)#id
    NickName = models.CharField(max_length=15)#昵称
    Password = models.CharField(max_length=25)#密码
    Email=models.EmailField()#邮箱
    Phone_number = models.CharField(max_length=17, blank=True)#手机号
    Profile_photo = models.ImageField(upload_to='profile_photos/')#头像
    Register_time = models.DateTimeField()#注册时间
    def __str__(self):
        return self.User_ID