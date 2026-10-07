from rest_framework import serializers

from VRclub.models import Genre
from VRclub.models import Game
from VRclub.models import GenreInGame
from VRclub.models import GameSet
from VRclub.models import GameOnSet
from VRclub.models import Hall
from VRclub.models import Order
from VRclub.models import OrderItem


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class GenreInGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreInGame
        fields = '__all__'


class GameSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSet
        fields = '__all__'


class GameOnSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameOnSet
        fields = '__all__'


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
