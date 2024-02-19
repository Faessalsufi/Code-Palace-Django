from django.urls import path
from . import views

app_name = "CodePalaceBase"

urlpatterns = [
    path('', views.home, name="home"),

    # CRUD operations
    path('questions/', views.QuestionListView.as_view(), name="questions_list"),
    path('questions/<int:pk>/', views.QuestionDetailView.as_view(),
         name="questions_detail"),

    path('questions/create', views.QuestionCreateView.as_view(),
         name="question_create"),
    # added
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(),
         name="profiles"),

]
