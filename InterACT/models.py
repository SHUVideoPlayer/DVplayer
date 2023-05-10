import video.models as videomodels
import User.models as Usermodels

# Create your models here.
from django.db import models


class Like_Favorite_Table(models.Model):
    type_choices = (("like", "点赞"), ("favorite", "收藏"))

    Act_id = models.AutoField(primary_key=True)
    User = models.Foreignkey(Usermodels.User)
    Type = models.CharField(choices=type_choices)
    DV = models.ForeignKey(videomodels.Video)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['User', 'Type', 'DV'],
                name='unique_act'
            )
        ]

    def __str__(self):
        return self.User + ' ' + self.Type + ' ' + self.DV


class Attention_Table(models.Model):
    Attention_id = models.AutoField(primary_key=True)
    User = models.Foreignkey(Usermodels.User)
    Up = models.Foreignkey(Usermodels.User)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['User', 'Up'],
                name='unique_act'
            )
        ]

    def __str__(self):
        return self.User + ' ' + self.Up


class Comment_Table(models.Model):
    Comment_id = models.AutoField(primary_key=True)
    User = models.Foreignkey(Usermodels.User)
    Comment = models.CharField(max_length=None, verbose_name="评论")
    Time = models.TimeField(auto_now_add=True, verbose_name="创建时间")
    DV = models.ForeignKey(videomodels.Video)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['User', 'Comment', 'Time', 'DV'],
                name='unique_act'
            )
        ]

    def __str__(self):
        return self.DV + ' ' + self.User + ':' + self.Comment
