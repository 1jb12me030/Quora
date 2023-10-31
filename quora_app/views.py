from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from .models import Question, Answer, Like
from .forms import QuestionForm, AnswerForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('view_questions')
    else:
        form = UserRegistrationForm()
    return render(request, 'quora_app/register_user.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('view_questions')
    else:
        form = AuthenticationForm()
    return render(request, 'quora_app/login_user.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('view_questions')


def view_questions(request):
    questions = Question.objects.all()
    return render(request, 'quora_app/view_questions.html', {'questions': questions})

def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('view_questions')
    else:
        form = QuestionForm()
    return render(request, 'quora_app/post_question.html', {'form': form})

def answer_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('view_questions')
    else:
        form = AnswerForm()
    return render(request, 'quora_app/answer_question.html', {'form': form, 'question': question})

def like_answer(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    like, created = Like.objects.get_or_create(user=request.user, answer=answer)
    if not created:
        like.delete()
    return redirect('view_questions')
