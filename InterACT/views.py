from django.shortcuts import render
import User.views as Userviews
import InterACT.models as IACTmodels
import video.models as videomodels
import User.models as Usermodels


# Create your views here.
def view_test(request):
    return render(request, 'Comment_view.html')


def comment_view(request, DV_code):
    comment_list = IACTmodels.Comment_Table.objects.filter(DV=videomodels.Video.objects.get(DVcode=DV_code))
    context = {
        "Comment", comment_list
    }
    return render(request, 'Comment_view.html', context)


def comment_add(request, DV_code):
    Userviews.islogin(request)
    return render(request, 'Comment_view.html')
