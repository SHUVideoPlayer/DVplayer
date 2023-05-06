from django.db import models

# Create your models here.
from django.db import models

class Like_Favorite_Table(models.Model):

    type_choices = (("like", "点赞"), ("favorite", "收藏"))

    user = models.CharField(max_length=100)#
    type = models.CharField(choices=type_choices)
    DV = models.CharField(max_length=100)#

class Attention_Table(models.Model):

    user = models.CharField(max_length=100)#
    up = models.CharField(max_length=100)#

class Comment_Table(models.Model):

    user = models.CharField(max_length=100)#
    comment = models.CharField(max_length=None, verbose_name="评论")
    time = models.TimeField(auto_now_add=True, verbose_name="创建时间")
    DV = models.CharField(max_length=100)#
