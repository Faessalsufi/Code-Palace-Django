from django.views.generic import DetailView
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Question
from CodePalaceUsers.models import Profile
from django.urls import reverse

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


class QuestionCreateView(CreateView):
    model = Question
    fields = ['title', 'content']
    template_name = 'CodePalaceBase/question_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Assuming the profile page URL is named 'profile'
        return reverse('CodePalaceBase:questions_detail', kwargs={'pk': self.object.pk})

    # added


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'codepalaceUsers/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.object.user
        return context
