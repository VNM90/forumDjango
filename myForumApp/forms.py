from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Question, ForumUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=60, help_text='Required. Add a valid email adress')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {'user': forms.HiddenInput()}


# class LoginForm(AuthenticationForm):
#     pass

# class Meta:
#     model = User
#     fields = '__all__'

class ForumUserForm(ModelForm):
    class Meta:
        model = ForumUser
        fields = '__all__'
        exclude = ['user']
