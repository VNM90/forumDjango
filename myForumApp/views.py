from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Question, ForumUser
from .forms import RegistrationForm, QuestionForm, ForumUserForm
from django.contrib.auth.models import User


def homeView(request):
    all_questions = Question.objects.all()
    all_catergories = Category.objects.all()
    return render(request, 'home.html', {'all_categories': all_catergories, 'all_questions': all_questions})


def categoryView(request, categoryId):
    all_catergories = Category.objects.all()
    category = get_object_or_404(Category, pk=categoryId)
    category_question = Question.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'category_question': category_question, 'all_categories': all_catergories})


def questionView(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    return render(request, 'question.html', {'question': question})


@login_required
def createView(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeView')
    else:
        user = get_user(request)
        form = QuestionForm(initial={'user': user})
    return render(request, 'create.html', {'form': form})


@login_required
def updateView(request, updateId):
    obj = get_object_or_404(Question, pk=updateId, user=request.user)
    form = QuestionForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('homeView')

    return render(request, 'create.html', {'form': form})


@login_required
def deleteView(request, deleteId):
    delete_question = get_object_or_404(
        Question, pk=deleteId, user=request.user)
    if request.method == "POST":
        delete_question.delete()
        return redirect('homeView')
    return render(request, "delete.html")


def loginView(request):
    if request.user.is_authenticated:
        return redirect('homeView')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('homeView')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def registerView(request):
    if request.user.is_authenticated:
        return redirect('homeView')
    else:
        form = RegistrationForm()
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                ForumUser.objects.create(
                    user=user,
                )
                messages.success(request, 'New user added')
                return redirect('homeView')
            else:
                messages.info(request, 'Username or password is incorrect')

        return render(request, 'register.html', {'form': form})


@login_required
def logoutView(request):
    logout(request)
    return redirect('homeView')


@login_required
def settingsView(request, user):
    forum_user = ForumUser(request.user)
    return render(request, 'settings.html', {'forum_user': forum_user})
