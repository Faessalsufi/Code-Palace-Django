from django.views.generic import DetailView
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
    template_name = 'codepalaceUsers/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.object.user
        return context
