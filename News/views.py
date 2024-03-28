from django.shortcuts import render, redirect
from .forms import NewsForm
from .models import News
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def NewsPage(request):
    news = News.objects.values()
    return render(request, 'news.html', {'News':news})

@login_required(login_url='login')
def addNews(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news_instance = form.save(commit=False)
            news_instance.author = request.user
            news_instance.save()
            return redirect('news')
        else:
            print("очен очен очен очен очен очен очен оибка", form)
    else:
        form = NewsForm()
    return render(request, 'AddNews.html', {'form': form})

def registration(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('news') 
        else:
            print("не работает иди нафиг", form)
    return render(request, 'registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('news')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})