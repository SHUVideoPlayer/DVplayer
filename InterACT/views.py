from django.shortcuts import render
import User.views as Userviews
import InterACT.models as IACTmodels
import video.models as videomodels
import User.models as Usermodels
import math
from django.http import JsonResponse
import datetime


def comment(request):
    #此处的userId 与 DV号需要作为参数传入
    userId = '1'
    DVId = '1'
    row = IACTmodels.Like_Favorite_Table()
    user = Usermodels.User.objects.get(User_ID=userId)
    DV = videomodels.Video.objects.get(DVcode=DVId)

    # 点赞数量
    likeCount = IACTmodels.Like_Favorite_Table.objects.filter(Type="like", User=user, DV=DV).count()

    # 收藏数量
    favorite = IACTmodels.Like_Favorite_Table.objects.filter(Type="favorite", User=user, DV=DV).count()

    # 是否点赞
    likeRow = IACTmodels.Like_Favorite_Table.objects.filter(Type="like", User=user, DV=DV).first()

    # 是否收藏
    favoriteRow = IACTmodels.Like_Favorite_Table.objects.filter(Type="favorite", User=user, DV=DV).first()

    #分页
    page = request.GET.get('page')
    pagesize = 5
    pagecount = range(1,
                      math.ceil(IACTmodels.Comment_Table.objects.order_by('-Comment_id').count() / pagesize) + 1)
    if page is None:
        page = 1
    page = int(page)

    commentList = IACTmodels.Comment_Table.objects.order_by('-Comment_id').all()[
                  ((page - 1) * pagesize):page * pagesize]

    return render(request, 'comment.html', {
        'userId': userId,
        'DV': DVId,
        'likeCount': likeCount,
        'favorite': favorite,
        'likeRow': likeRow,
        'favoriteRow': favoriteRow,
        'commentList': commentList,
        'pagecount': pagecount
    })

#修改评论和点赞
def commentChangeStatus(request):

    #获取页面的相关信息，在创建页面时传入
    userId = request.GET.get('userId')
    DVId = request.GET.get('DV')
    type = request.GET.get('type')
    status = request.GET.get('status')

    #如果当前未点赞或收藏，添加记录
    if status == '1':
        row = IACTmodels.Like_Favorite_Table()
        row.User = Usermodels.User.objects.get(User_ID=userId)
        row.Type = type
        row.DV = videomodels.Video.objects.get(DVcode=DVId)
        row.save()
    #如果当前点赞或收藏，删除记录
    else:
        IACTmodels.Like_Favorite_Table.objects.filter(Type=type, User=Usermodels.User.objects.get(User_ID=userId), DV=videomodels.Video.objects.get(DVcode=DVId)).delete()

    data = {
        'code': 0,
        'msg': '成功',
        'data': {
            'count': IACTmodels.Like_Favorite_Table.objects.filter(Type=type, User=Usermodels.User.objects.get(User_ID=userId), DV=videomodels.Video.objects.get(DVcode=DVId)).count()
        }
    }
    return JsonResponse(data)

#发表评论
def commentEdit(request):
    id = request.GET.get('id')
    userId = request.GET.get('userId')
    DVId = request.GET.get('DV')
    comment = request.GET.get('comment')
    type = request.GET.get('type')

    if type == '0':
        row = IACTmodels.Comment_Table()
        row.User = Usermodels.User.objects.get(User_ID=userId)
        row.Comment = comment
        row.Time = datetime.datetime.now().strftime("%Y-%m-%d %X")
        row.DV = videomodels.Video.objects.get(DVcode=DVId)
        row.save()

    if type == '1':
        IACTmodels.Comment_Table.objects.filter(Comment_id=id).update(Comment=comment)

    data = {
        'code': 0,
        'msg': '成功'
    }

    return JsonResponse(data)

#删除评论
def commentDelete(request):
    IACTmodels.Comment_Table.objects.filter(Comment_id=request.GET.get('id')).delete()
    data = {
        'code': 0,
        'msg': '成功'
    }
    return JsonResponse(data)