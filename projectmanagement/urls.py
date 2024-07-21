from django.urls import path, re_path, include
from django.shortcuts import redirect
from django.contrib import admin
from . import views

urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    # home
    path("", views.home, name="home"),
    # auth
    # path('auth/login', views.auth_login, name='auth_login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('auth/register', views.auth_register, name='auth_register'),
    # re_path(r'^auth.*$', lambda request: redirect('auth_login', permanent=True)),
    # game
    path('game', views.game, name='game_index'),
    path('game/start', views.game_play, name='game_play'),
    path('game/end', views.game_end, name='game_end'),
    path('game/history', views.game_history, name='game_history'),
    path('game/rank', views.game_rank, name='game_rank'),
    # user
    path('profile', views.user_profile, name='user_profile'),
    path('profile/<int:user_id>', views.user_detail, name='user_detail'),
    # language switcher
    path('switch-language/<str:language_code>/', views.switch_language, name='switch_language'),
]
