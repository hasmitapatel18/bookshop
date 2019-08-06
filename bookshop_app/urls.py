from django.urls import path
from . import views
from bookshop_app.views import *



urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('register/', views.RegisterView.as_view(), name='register'),




]
