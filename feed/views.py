from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, FormView
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
            image = form.cleaned_data['image']
        )
        messages.add_message(self.request, messages.SUCCESS, "Your post was Uploaded")
        return super().form_valid(form)