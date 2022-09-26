from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url = 'login')
def home(request):
    userdetail = User.objects.get(id=request.user.id)
    return render(request, 'dashboard/home.html', {"userdetail":userdetail})

def signup(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get('lastname')
        Profile_Picture = request.FILES["profile_picture"]
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        user_type = request.POST.get('user_type')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already exists')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, Profile_Picture=Profile_Picture, email=email, username=username, password=password, address=address, city=city, state=state,pincode=pincode, user_type=user_type)
                    user.save()
                    messages.success(request, "account created successfully")
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect("signup")

    return render(request, 'dashboard/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')

    return render(request, 'dashboard/login.html')

@login_required(login_url = 'login')
def profile(request):
    userdetail = User.objects.get(id=request.user.id)
    print(userdetail)
    return render(request, 'dashboard/profile.html', {"userdetail":userdetail})

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are successfully logout")

    return redirect('home')

