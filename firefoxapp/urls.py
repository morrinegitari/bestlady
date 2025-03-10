from django.contrib import admin
from django.urls import path
from firefoxapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('', views.register,name='register'),
    path('login', views.login_view,name='login'),
]

