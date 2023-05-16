from django.contrib import admin
from .models import Like_Favorite_Table
from .models import Attention_Table
from .models import Comment_Table

# Register your models here.
admin.site.register(Like_Favorite_Table)
admin.site.register(Attention_Table)
admin.site.register(Comment_Table)