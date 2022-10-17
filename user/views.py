from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'GET':
            return render(request, 'user/signup.html')
    elif request.method == 'POST':
        user_id = request.POST.get('user_id', None)
        user_password = request.POST.get('user_password', None)
        user_password2 = request.POST.get('user_password2', None)
        user_name = request.POST.get('user_name', None)
        user_email = request.POST.get('user_email', None)
        user_phone = request.POST.get('user_phone', None)

        exist_user = get_user_model().objects.filter(username=user_id)

        if user_password != user_password2:
            msg = '비밀번호가 일치하지 않습니다.'
            return render(request, 'user/signup.html', {'message': msg})
        elif exist_user:
            msg = '이미 존재하는 아이디입니다.'
            return render(request, 'user/signup.html', {'message': msg})
        else:
            User.objects.create_user(username=user_id, password=user_password, user_name=user_name, email=user_email, phone=user_phone)
            return redirect('/user/signin/')


def signin(request):
    if request.method == 'GET':
            return render(request, 'user/signin.html')
    elif request.method == 'POST':
        user_id = request.POST.get('user_id', None)
        user_password = request.POST.get('user_password', None)

        me = auth.authenticate(request, username=user_id, password=user_password)
        if me is not None:
            auth.login(request, me)
            return redirect('/post/main')
        else:
            msg = '아이디 혹은 비밀번호 정보가 잘못되었습니다.'
            return render(request, 'user/signin.html', {'message': msg})