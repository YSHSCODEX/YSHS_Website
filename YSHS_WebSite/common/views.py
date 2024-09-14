from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import login, authenticate
from .forms import CustomUserForm
from .models import CustomUser

def signup(request):
    return render(request, 'mainPage/home.html')

def signup(request):
    print(request.method)
    if request.method == "POST":
        form = CustomUserForm(request.POST) # CustomUserForm 사용할거임
        if form.is_valid():
            user = form.save()  # 사용자 생성
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)   # 사용자 인증
            if user is not None:
                login(request, user)    # 로그인 처리
                return redirect('mainPage:home')
    else:
        form = CustomUserForm()
    
    return render(request, 'common/signUp.html', {'form' : form})