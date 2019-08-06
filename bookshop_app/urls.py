from django.urls import path
from . import views
from bookshop_app.views import *



urlpatterns = [
    # path('', FilmListView.as_view(), name='film_list'),
    path('register/', views.RegisterView.as_view(), name='register'),




]
