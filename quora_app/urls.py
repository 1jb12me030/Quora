from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.view_questions, name='view_questions'),
    path('post/', views.post_question, name='post_question'),
    path('answer/<int:question_id>/', views.answer_question, name='answer_question'),
    path('like/<int:answer_id>/', views.like_answer, name='like_answer'),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
]
