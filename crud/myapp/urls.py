from django.urls import path
from .import views

urlpatterns = [
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('index/', views.index, name="index.html" ),
    path('add/',views.add,name="add"),
    path('addrec/', views.addrec, name="addrec"),
    path('index/delete/<int:id>/', views.delete, name="delete"), 
    path('index/update/<int:id>/', views.update, name="update"), 
    path('update/uprec/<int:id>/', views.uprec, name="uprec"), 
    path('logout/',views.LogoutPage,name='logout'),
]
