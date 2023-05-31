from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('blogs', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<int:num>', views.show, name='blog_show'),
    path('<int:num>/edit', views.edit, name='blog_edit'),
    path('<int:num>/delete', views.destroy, name='blog_delete'),
    path('json', views.json)
]
