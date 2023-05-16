import video.models as videomodels
import User.models as Usermodels

# Create your models here.
from django.db import models


class Like_Favorite_Table(models.Model):
    type_choices = (("like", "点赞"), ("favorite", "收藏"))

    Act_id = models.AutoField(primary_key=True)
    User = models.ForeignKey(Usermodels.User, related_name='+', on_delete=models.CASCADE)
    Type = models.CharField(choices=type_choices, max_length=255)
    DV = models.ForeignKey(videomodels.Video, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return self.User + ' ' + self.Type + ' ' + self.DV


class Attention_Table(models.Model):
    Attention_id = models.AutoField(primary_key=True)
    User = models.ForeignKey(Usermodels.User, related_name='+', on_delete=models.CASCADE)
    Up = models.ForeignKey(Usermodels.User, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return self.User + ' ' + self.Up


class Comment_Table(models.Model):
    Comment_id = models.AutoField(primary_key=True)
    User = models.ForeignKey(Usermodels.User, related_name='+', on_delete=models.CASCADE)
    Comment = models.CharField(max_length=1023, verbose_name="评论")
    Time = models.CharField(max_length=255)
    DV = models.ForeignKey(videomodels.Video, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return self.DV + ' ' + self.User + ':' + self.Comment
