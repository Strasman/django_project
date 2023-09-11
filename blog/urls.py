from django.urls import path
from blog import views

urlpatterns = [
    path('time/', views.today_is, name='todays_time'),
    path('h', views.index, name='blog_index'),
    path('blog/', views.test_redirect, name='test_redirect'),
    path('feedback/', views.feedback, name='feedback'),
    path('cookie/', views.test_cookie, name='cookie'),
    path('track_user/', views.track_user, name='track_user'),
    path('stop-tracking/', views.stop_tracking, name='stop_tracking'),
    path('test-session/', views.test_session, name='test_session'),
    path('test-delete/', views.test_delete, name='test_delete'),
    path('save-session-data/', views.save_session_data, name='save_session_data'),
    path('access-session-data/', views.access_session_data, name='access_session_data'),
    path('delete-session-data/', views.delete_session_data, name='delete_session_data'),
    path('lousy-login/', views.lousy_login, name='lousy_login'),
    path('lousy-secret/', views.lousy_secret, name='lousy_secret'),
    path('lousy-logout/', views.lousy_logout, name='lousy_logout'),
    path('category/<slug:category_slug>/', views.post_by_category, name='post_by_category'),
    path('tag/<slug:tag_slug>/', views.post_by_tag, name='post_by_tag'),
    path('<int:pk>/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('', views.post_list, name='post_list'),
]
