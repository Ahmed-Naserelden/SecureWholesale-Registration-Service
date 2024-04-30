from django.urls import path, include
from . import views

urlpatterns = [    
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),

    path('users/', views.users_list, name='user_list'),
    path('users/<str:pk>/', views.user, name='user'),
    
    path('organizations/', views.organizations_list, name='org_list'),
    path('organizations/<str:pk>/', views.organization, name='organization'),
    
    path('permissions/', views.permissions_list, name='perm_list'),
    path('permissions/<str:pk>/', views.permission, name='permission'),

    path('change-password/', views.change_password),

]


