from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import UserUpdateForm, ProfileUpdateForm


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


@login_required
def profile_update(request):
    if request.method == "POST":
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, f'Profile Updated!')
            return redirect('profile')
        else:
            # Set initial values based on current user data
            initial = {
                'username': request.user.username,
                'email': request.user.email,
                'bio': request.user.profile.bio,
                'phone': request.user.profile.phone,
            }
            user_update_form.initial = initial
            profile_update_form.initial = initial
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form
    }
    return render(request, 'codepalaceUsers/profile_update.html', context)
