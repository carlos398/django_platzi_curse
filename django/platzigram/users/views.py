"""users views"""

#Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

#models
from django.contrib.auth.models import User
from users.models import Profile

def login_view(request):
    """login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('feed')
        else:
            return render(request,'users/login.html', {'error': 'invalid username and password'})

    return render(request, 'users/login.html')


def signup(request):
    """signup"""
    if request.method == 'POST':
        username = request.POST['username']
        psswd = request.POST['password']
        psswd_confirmation = request.POST['password_confirmation']

        if psswd != psswd_confirmation:
            return render(request, 'users/signup.html', {'error': 'passwprd confirmation does not match'})
        
        user = User.objt.create_user(username=username, password=psswd)
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.femail = request.POST['email']

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')


@login_required
def logout_view(request):
    """logout a user"""
    logout(request)
    return redirect('login')