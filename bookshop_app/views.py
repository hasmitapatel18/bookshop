from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *

from .forms import *

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView, FormMixin

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView

from django.shortcuts import get_object_or_404

from django.contrib.auth import login, logout, authenticate

from django.contrib import messages

from django.forms import inlineformset_factory

from django.http import HttpResponse, HttpResponseRedirect

from django.db import transaction

from cloudinary.forms import cl_init_js_callbacks

import cloudinary

import cloudinary.uploader

import cloudinary.api


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'bookshop_app/register.html'


class BookListView(ListView):
    template_name = 'bookshop_app/book_list.html'
    context_object_name='books'
    model=Book_entry

    def get_queryset(self):
        return Book_entry.objects.all()
