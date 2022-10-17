from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def main(request):
    if request.method == 'GET':
        is_user = request.user.is_authenticated
        if is_user:
            user=request.user
        return render(request, 'post/main.html', context=dict(user=user))

def upload(request):
    if request.method == 'POST':
        post = Post()
        post.user = request.user
        post.image = request.FILES.get('img')
        post.save()
        return redirect('/post/main')