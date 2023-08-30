from django.urls import path
from base.views import home, fetch_posts, create_post, update_post, view_post, delete_post, view_profile, send_email

urlpatterns = [
    path('', home, name='home'),
    path('posts/', fetch_posts, name='posts'),
    path('post/<slug:slug>/', view_post, name='post'),
    path('profile/', view_profile, name='profile'),

    # CRUD PATHS

    path('create_post/', create_post, name='create_post'),
    path('update_post/<slug:slug>/', update_post, name='update_post'),
    path('delete_post/<slug:slug>/', delete_post, name='delete_post'),


    path('send_email/', send_email, name='send_email'),
]
