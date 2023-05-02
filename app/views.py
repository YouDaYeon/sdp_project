from .models import User
from django.shortcuts import render, redirect as r
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.utils import timezone
from django.contrib.auth import logout


# Create your views here.
# HOME
def home(request):
    users = User.objects.all()
    context = {'data':users}
    return render(request,'app/home.html',context=context)

# 일기장
def diary(request):
    today = datetime.today().date()
    context={"date":today}
    return render(request,'app/diary.html',context=context)

# 로그인
def user_signin(request):
  # Post 으로 요청했을 때
  if request.method == 'POST':
    # name = request.POST.get('name')
    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    try:
    #   User.objects.get(email=email, pwd=encrypt(pwd))
      user = User.objects.get(email=email, pwd=pwd)
      name = user.name
      request.session['name'] = name
    except:  # 이메일 또는 비밀번호가 일치하지 않을때
      return r('/app/user/signin/')
    
    return r('/app/home/')
  # Get 으로 요청했을 때
  return render(request, 'app/signin.html', {})

# 로그아웃
def user_logout(request):
    logout(request)
    return r('/app/home/')

# 회원가입
def user_signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        u = User()
        u.email = email
        u.name = name
        u.pwd = pwd
        u.c_date = timezone.now()
        # u.c_date = da tetime.datetime.now()
        u.save()

        # return HttpResponse(
        #   '<script>location="/first/user/signup/"</script>'
        # )

        # return r('/app/user/signup/')

        return HttpResponse(
        '%s님 가입 감사합니다.' % name)


    # Get으로 요청했을 때
    return render(request, 'app/signup.html')

# 유튜브
def youtube(request):
    today = datetime.today().date()
    context={"date":today}
    return render(request,'app/youtube.html',context=context)

# 뉴스
def news(request):
    today = datetime.today().date()
    context={"date":today}
    return render(request,'app/news.html',context=context)

# 달력
def calendar(request):
    today = datetime.today().date()
    context={"date":today}
    return render(request,'app/calendar.html',context=context)

# todolist
def todolist(request):
    today = datetime.today().date()
    context={"date":today}
    return render(request,'app/todolist.html',context=context)

# book
def book(request):
    today = datetime.today().date()
    context={"date":today}
    return render(request,'app/book.html',context=context)