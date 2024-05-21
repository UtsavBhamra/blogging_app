from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('blogs/<int:id>',views.full_post,name='full_post')
]
