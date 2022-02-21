from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    DeleteView,
    UpdateView
)

from .forms import ArticleForm
from .models import Article

# Here we use class based views
class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()
    
    def form_valid(self, form): # Just to be able to print-debug
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleListView(ListView):
    template_name = 'articles/article_list.html' # <app_name>/<modelname>_list.html django will by default look for but here we provide the exact file
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    # For a detail view queryset is no longer the entire list to view but it's a limitation of which specific element to view (the queryset must contain that element)
    #queryset = Article.objects.filter(id__gt=1) I think this is only relevant if we use the default way not our own get_object?
    def get_object(self): # If we didn't include this DetailView has a default way of getting the object which is to look for a parameter pk
        id_ = self.kwargs.get("id") # # pk is short for primary key
        return get_object_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html' # Not that we can use the same template the only difference between the views is basically the get object
    form_class = ArticleForm
    queryset = Article.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get("id") # # pk is short for primary key
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form): # Just to be able to print-debug
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')