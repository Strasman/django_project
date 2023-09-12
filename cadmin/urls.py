from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
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
    path('post/delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('category/', views.category_list, name='category_list'),
    path('category/add/', views.category_add, name='category_add'),
    path('category/update/<int:pk>/', views.category_update, name='category_update'),
    path('category/delete/<int:pk>/', views.category_delete, name='category_delete'),
    path('tag/', views.tag_list, name='tag_list'),
    path('tag/add/', views.tag_add, name='tag_add'),
    path('tag/update/<int:pk>/', views.tag_update, name='tag_update'),
    path('tag/delete/<int:pk>/', views.tag_delete, name='tag_delete'),
    path('account-info/', views.account_info, name='account_info'),
]