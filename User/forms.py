from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Profile_photo','NickName','User_ID','Password','Email','Phone_number',]
        labels = {'Profile_photo':'头像','NickName':'昵称','User_ID':'用户名','Password':'密码','Email':'邮箱','Phone_number':'手机号',}
