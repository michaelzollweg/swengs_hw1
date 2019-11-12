from rest_framework import serializers
from swengs.hw1_zollweg.models import Game

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ['name', 'genre', 'year', 'multiplayer', 'price']