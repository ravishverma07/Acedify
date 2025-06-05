from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', user_list, name='user_list'),
    path('chat/<str:username>/', chat, name='chat'),

]