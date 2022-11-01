from django.shortcuts import render,redirect
from .forms import signupForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


def accounts(request):
    form = signupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    else:
        if request.POST.get('confirm_password') != request.POST.get('password'):
            messages.error(request, "Password Doesn't match")
        else:
            form.errors
    context = {'signup':form}
    return render(request, 'accounts/accounts.html', context)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        raw_password = request.POST.get('password')
        user = authenticate(username=username, password=raw_password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                print('superuser')
            elif not user.is_superuser:    
                login(request, user)
                print('logged in!')
        else:
            return redirect('accounts:login')
    return render(request, 'accounts/login.html')
