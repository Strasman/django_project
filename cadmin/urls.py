from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', auth_views.LoginView.as_view(template_name='cadmin/login.html'),
        name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='cadmin/logout.html'),
        name='logout'),
    path('password-change-done/',
        auth_views.PasswordChangeDoneView.as_view(template_name='cadmin/password_change_done.html'),
        name='password_change_done'),
    path('password-change/',
        auth_views.PasswordChangeView.as_view(
            template_name='cadmin/password_change.html',
            success_url='password_change_done'  # Use the URL name for success_url
         ),
         name='password_change'),
    path('register/', views.register, name = 'register'),
    path('activate/account/', views.activate_account, name = 'activate'),
    path('post/add/', views.post_add, name = 'post_add'),
    path('post/update/<int:pk>/', views.post_update, name='post_update'),
]