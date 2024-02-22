from django.views.generic import DetailView
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Question
from CodePalaceUsers.models import Profile
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse
from django.views.generic.edit import DeleteView


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


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['title', 'content']
    template_name = 'CodePalaceBase/question_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class QuestionUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['title', 'content']
    template_name = 'CodePalaceBase/question_create.html'

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        else:
            return False


class QuestionDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Question

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        else:
            return False

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request, 'Your post has been deleted successfully.')
        return response

    def get_success_url(self):
        return reverse('CodePalaceBase:questions_list')

    # added


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'codepalaceUsers/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.object.user
        return context
