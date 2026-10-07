from django.contrib import admin

from VRclub.models import Profile
from VRclub.models import Genre
from VRclub.models import Game
from VRclub.models import GenreInGame
from VRclub.models import GameSet
from VRclub.models import GameOnSet
from VRclub.models import Hall
from VRclub.models import Order
from VRclub.models import OrderItem


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'role']

    def has_add_permission(self, request):
        return False


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


@admin.register(GenreInGame)
class GenreInGameAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_game', 'id_genre']


@admin.register(GameSet)
class GameSetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price_per_hour']


@admin.register(GameOnSet)
class GameOnSetAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_game', 'id_game_set']


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'capacity', 'price_per_hour']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'total_amount', 'status']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_order', 'id_hall', 'id_game_set', 'start_time']
