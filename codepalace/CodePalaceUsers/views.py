from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account Successfully Created For {username}')
            # Auto log in the user
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'])
            login(request, user)

            return redirect('CodePalaceBase:home')
    else:
        form = UserRegisterForm()

    return render(request, 'codepalaceUsers/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'codepalaceUsers/profile.html')
