from django.contrib import admin
from swengs.hw1_zollweg.models import Game
# Register your models here.

class GameModel(admin.ModelAdmin):
    list_display = ('name', 'genre','year')


admin.site.register(Game, GameModel)