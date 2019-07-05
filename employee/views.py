from django.shortcuts import render, redirect ,HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, login
from django.urls import reverse
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm

# Create your views here.


def employee_listing(request):
    if request.user.is_authenticated:
        employees = User.objects.all()
        return render(request, 'employee_listing.html', {'employees': employees})
    else:
        return redirect('login')

def signup(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')

    else:
        f = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': f})


def account_view(request):
    user = request.user
    return render(request, 'account.html', {'user': user})


def account_edit(request):
    form = CustomUserChangeForm(request.POST, instance=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect(reverse('account_view'))
    else:
        form = CustomUserChangeForm(instance=request.user)
        return render(request, 'account_edit.html', {'form': form})


def update_password(request):
    form = CustomPasswordChangeForm(request.user, request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password Changed!!')
            return redirect('account_view')
        else:
            messages.error(request, "Try Again")
            return render(request, 'update_password.html', {'form': form})
    else:
        form = CustomPasswordChangeForm(request.user)
        return render(request, 'update_password.html', {'form': form})

