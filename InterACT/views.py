from django.shortcuts import render

# Create your views here.
def view_test(request):
    return render(request, 'Comment_view.html')

def comment_view(request):
    return render(request, 'Comment_view.html')