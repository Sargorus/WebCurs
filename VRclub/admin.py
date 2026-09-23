from django.contrib import admin

from VRclub.models import Genre
from VRclub.models import Game
from VRclub.models import Genre_in_game
from VRclub.models import Hall
from VRclub.models import Order
from VRclub.models import OrderItem
# Register your models here.

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name','description']

@admin.register(Game)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name','description']

@admin.register(Genre_in_game)
class Genre_in_gameAdmin(admin.ModelAdmin):
    list_display = ['id_game','id_genre']

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = []