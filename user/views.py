from django.shortcuts import render, redirect

# Create your views here.
def signup(request):
    if request.method == 'GET':
            return render(request, 'user/signup.html')

def signin(request):
    if request.method == 'GET':
            return render(request, 'user/signin.html')