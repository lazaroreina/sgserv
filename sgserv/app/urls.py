from django.urls.conf import path
from . import views

urlpatterns= [ 
    path('lista', views.lista, name='lista'),
]