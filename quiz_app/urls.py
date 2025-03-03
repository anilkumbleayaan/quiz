from django.urls import path
from .views import login_view, logout_view, instruction_view, quiz_view, system_compatibility_view, submit_quiz
from . import views
from .views import register

urlpatterns = [
     path('', views.login_view, name='login'),   # This is calling index.html by default
    path('login/', views.login_view, name='login'),  # Ensure login URL exists
    path('logout/', views.logout_view, name='logout'),
    # path('register/', views.register_view, name='register'), 
    path("register/", register, name="register"),
    path('instruction/', instruction_view, name='instruction'),  # New instruction page
    path('quiz/', quiz_view, name='quiz'),
    path('system-compatibility/', system_compatibility_view, name='system_compatibility'),
    path("submit/", submit_quiz, name="submit_quiz"),
]
