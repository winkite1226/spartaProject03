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

        exist_user = get_user_model().objects.filter(user_id=user_id)

        if user_password != user_password2:
            msg = '비밀번호가 일치하지 않습니다.'
            return render(request, 'user/signup.html', {'message': msg})
        elif exist_user:
            msg = '이미 존재하는 아이디입니다.'
            return render(request, 'user/signup.html', {'message': msg})
        else:
            User.objects.create_user(user_id=user_id, password=user_password, username=user_name, email=user_email, phone=user_phone)
            return redirect('/signin/')


def signin(request):
    if request.method == 'GET':
            return render(request, 'user/signin.html')