import datetime
from typing import Any
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import DetailView, TemplateView, FormView, ListView, DeleteView
from .forms import PostForm
from .models import Post
# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        content =  super().get_context_data(**kwargs)
        content['post'] = Post.objects.all().order_by('-id')
        return content
    
class DetailView(DetailView):
    template_name = 'details.html'
    model = Post
    
class PostView(FormView):
    template_name = 'post.html'
    success_url = '/'
    form_class = PostForm
    
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
        
    def form_valid(self, form):
        new_object = Post.objects.create(
            text = form.cleaned_data['text'],
            image = form.cleaned_data['image'],
         #   date = str(datetime.datetime.now()),
        )
        messages.add_message(self.request, messages.SUCCESS, "Your post was Uploaded")
        return super().form_valid(form)
    
class SearchView(ListView):
    model = Post
    template_name = 'search_results.html'
    
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Post.objects.filter(
            Q(text__icontains=query)
        )
        return object_list

class DeletePage(DeleteView):
    template_name = 'post_confirm_delete.html'
    model = Post
    success_url = '/'
    
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Your post was Deleted")
        return super().form_valid(form)
    
    