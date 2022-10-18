from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from .models import Post
from user.models import User

# Create your views here.
def main(request):
    if request.method == 'GET':
        is_user = request.user.is_authenticated
        if is_user:
            user=request.user  # 현재 접속자
            post_object_list = Post.objects.all().order_by('-id')  # post 테이블에 있는 모든 사진들
            post_list = []

            for post in post_object_list:  # 각 post에 대해 확인하기
                if post.user == user:
                    post_list.append(dict(image=post.image))

            return render(request, 'post/main.html', context=dict(user=user, posts=post_list))
        else:
            return redirect('/user/signin')

def upload(request):
    if request.method == 'POST':
        post = Post()
        post.user = request.user
        post.image = request.FILES.get('img')
        
        if post.image == '':
            print('빈칸')
        post.save()
        return redirect('/post/main')