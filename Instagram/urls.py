from django.conf.urls import url
from Instagram import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'register/', views.register, name='register'),
    url(r'delete/(\d+)', views.deleteImage, name='delete'),
   url(r'^like/(?P<id>\d+)/$', views.like, name='like'),
    url(r'login/', views.userlogin, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^view/all/$', views.images, name='images'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^search/', views.search, name="search"),
    url(r'^update/(?P<id>\d+)/$', views.update, name='update'),
    url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
    url(r'^user/(?P<id>\d+)/$', views.user, name='user'),
]