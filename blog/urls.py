from django.urls import path
from blog import views

urlpatterns = [
    path('time/', views.today_is, name='todays_time'),
    path('h', views.index, name='blog_index'),
    path('category/<slug:category_slug>/', views.post_by_category, name='post_by_category'),
    path('tag/<slug:tag_slug>/', views.post_by_tag, name='post_by_tag'),
    path('<int:pk>/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('', views.post_list, name='post_list'),
]
