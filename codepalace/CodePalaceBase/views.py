from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Question
from CodePalaceUsers.models import Profile
# Create your views here.


def home(request):
    return render(request, "home.html")


# CRUD operations

class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    ordering = ['-date_created']


class QuestionDetailView(DetailView):
    model = Question

    # added


class ProfileDetailView(DetailView):
    model = Profile
    context_object_name = 'profile'
