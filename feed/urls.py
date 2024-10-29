from django.urls import path
from .views import HomeView, DetailView, PostView
app_name = 'feed'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('details/<int:pk>/', DetailView.as_view, name='details'),
    path('post/', PostView.as_view(), name='post')
]