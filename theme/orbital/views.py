from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import New, Comment
from .forms import NewForm, CommentForm
from django.utils import timezone

# Create your views here.

class Home(TemplateView):

    template_name = "orbital/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = New.objects.all()
        return context


class Articles(DetailView): 
    model = New
    template_name = "orbital/articles.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = Comment.objects.all()
        context['now'] = timezone.now()
        context['articles'] = New.objects.all()
        context['form'] = CommentForm()
        return context

class Create(CreateView): 
    form_class = NewForm
    template_name = 'orbital/create.html'
    success_url = reverse_lazy('home')

class Update(UpdateView):
    model = New
    form_class = NewForm
    template_name = 'orbital/update.html'
    success_url = reverse_lazy('home')

class Delete(DeleteView):
    model = New
    template_name = 'orbital/delete.html'
    success_url = reverse_lazy('home')