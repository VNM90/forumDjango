from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name='homeView'),
    path('register/', registerView, name='registerView'),
    path('login/', loginView, name='loginView'),
    path('logout/', logoutView, name='logoutView'),
    path('create/', createView, name='createView'),
    path('question/<int:questionId>/', questionView, name='questionView'),
    path('category/<int:categoryId>/', categoryView, name='categoryView'),
    path('delete/<int:deleteId>/', deleteView, name='deleteView'),
    path('update/<int:updateId>/', updateView, name='updateView'),
    path('settings/<user>', settingsView, name='settingsView'),
]
