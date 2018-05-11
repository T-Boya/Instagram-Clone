from django.conf.urls import url
from Instagram import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'register/', views.register, name='register'),
    url(r'login/', views.userlogin, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^view/all/$', views.images, name='images'),
    url(r'^upload/$', views.upload, name='upload'),
]