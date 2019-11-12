from django.urls import path
from swengs.hw1_zollweg import views

urlpatterns = [
    path('games/', views.game_list),
    path('games/<int:pk>/', views.game_detail),
]