from django.urls import path
from . import views

urlpatterns = [
     
     path('home/',views.home,name='home'),
     
     path('admin_login/',views.admin_login,name='admin_login'),
     
     path('',views.Login,name='Login'),
     
     path('signup/',views.signup,name='signup'),
     
     path('admin_home/',views.admin_home,name='admin_home'),
     
     path('Logout/',views.Logout,name='Logout'),
     
     path('admin_Logout/',views.admin_Logout,name='admin_Logout'),
     
     path('add/',views.add,name='add'),
     
     path('edit/',views.edit,name='name'),
     
     path('update/<str:id>',views.update,name="update"),
     
     path('delete/<str:id>',views.delete,name="delete"),
     
     path('search/',views.search,name="search"),
     
     path('alert/',views.alert,name="alert"),


]
