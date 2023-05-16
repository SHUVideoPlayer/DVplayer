from django import forms
from .models import User
from django.core.exceptions import ValidationError
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Profile_photo','NickName','User_ID','Password','Email','Phone_number',]
        labels = {'Profile_photo':'头像','NickName':'昵称','User_ID':'用户名','Password':'密码','Email':'邮箱','Phone_number':'手机号',}


def avatar_file_size(value):
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('头像文件太大了，请限制在2M之内')



def background_file_size(value):
    limit = 6 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('头像文件太大了，请限制在6M之内')



class EditProfileForm(forms.ModelForm):
    '''
    NickName = forms.CharField(min_length=1, max_length=20, required=False,
                               error_messages={
                                   'min_length': '昵称至少4个字符',
                                   'min_length': '昵称不能多于20个字符',
                               },
                               widget=forms.TextInput())

    Profile_photo = forms.ImageField(required=False, validators=[avatar_file_size],
                              widget=forms.FileInput(attrs={'class': 'n'}))

    Background_photo = forms.ImageField(required=False, validators=[background_file_size],
                              widget=forms.FileInput(attrs={'class': 'n'}))

    Email = forms.EmailField(required=False,
                             error_messages={
                                 'invalid': '请输入有效的Email地址',
                             },
                             widget=forms.EmailInput())

    Phone_number = forms.CharField(min_length=11, max_length=11, required=False,
                             error_messages={
                                 'min_length': '请输入11位手机号',
                                 'max_length': '请输入11位手机号',
                             },
                             widget=forms.NumberInput())

    Signature = forms.CharField(min_length=1, max_length=100, required=False,
                               error_messages={
                                   'min_length': '昵称至少1个字符',
                                   'min_length': '昵称不能多于100个字符',
                               },
                               widget=forms.TextInput())

'''
    class Meta:
        model = User
        fields = ['NickName', 'Profile_photo', 'Background_photo', 'Email', 'Phone_number','Signature',]
        labels = {'NickName':'昵称', 'Profile_photo':'头像', 'Background_photo':'背景图片', 'Email':'邮箱', 'Phone_number':'手机号','Signature':'个性签名', }


