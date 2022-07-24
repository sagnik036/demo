from django.contrib import admin
from django.urls import include, path

# import myapp
from . import views 

urlpatterns = [
    path('', views.register),
    path('doctor', views.doctor),
    path('patient', views.user),
    path('signup', views.signup),
    path('register',views.user_register),
    path('dashboard',views.dashboard),
    path('login',views.login)
    # path('',include('myapp.urls'))
]
