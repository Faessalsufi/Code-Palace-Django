from django.urls import path
from . import views

app_name = "CodePalaceBase"

urlpatterns = [
    path('', views.home, name="home"),

    # CRUD operations
    path('questions/', views.QuestionListView.as_view(), name="questions_list"),
    path('questions/<int:pk>/', views.QuestionDetailView.as_view(),
         name="questions_detail"),

    # added
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(),
         name="profile_detail"),

]
