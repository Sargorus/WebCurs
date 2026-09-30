from django.contrib import admin

from VRclub.models import Profile
from VRclub.models import Genre
from VRclub.models import Game
from VRclub.models import GenreInGame
from VRclub.models import Hall
from VRclub.models import Order
from VRclub.models import OrderItem
from VRclub.models import GameOnSet
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name','description']

@admin.register(Game)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name','description']

@admin.register(GenreInGame)
class GenreInGameAdmin(admin.ModelAdmin):
    list_display = ['id_game','id_genre']

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', ' capacity', 'price_per_hour']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(GameOnSet)
class GameOnSetAdmin(admin.ModelAdmin):
    list_display = []