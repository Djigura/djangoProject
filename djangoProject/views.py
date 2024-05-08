from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('info')  # Замените 'home' на имя вашего URL-маршрута для главной страницы
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Замените 'home' на имя вашего URL-маршрута для главной страницы
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def info_view(request):
    # Здесь можно добавить логику для получения и обработки информации, которую вы хотите отобразить на странице
    return render(request, 'info.html')