from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.TextField("Название")
    description = models.TextField("Общее описание")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Game(models.Model):
    name = models.TextField("Название")
    description = models.TextField("Общее описание")
    poster = models.ImageField("Постер")


class Genre_in_game:
    id_genre = models.ForeignKey("Genre", on_delete=models.SET_NULL, null=True)
    id_game = models.ForeignKey("Game", on_delete=models.SET_NULL, null=True)

class Game_set:
    name = models.TextField("Название")
    description = models.TextField("Описание")
    price_per_hour = models.IntegerField("Цена в рублях за час")


class Game_on_set:
    id_game = models.ForeignKey("Game", on_delete=models.SET_NULL, null=True)
    id_gameSet = models.ForeignKey("Game_set", on_delete=models.SET_NULL, null=True)


class Hall:
    name = models.TextField("Наименование")
    description = models.TextField("Описание")
    capacity = models.IntegerField("Вместимость человек")
    price_per_hour = models.IntegerField("Цена за 1 час брони на 1 человека")


class Order:
    total_amount = models.IntegerField("Общая стоимость заказа")
    # Тут наверное стоит enum сделать
    status = models.TextField("Статус заказа")


class Order_item:
    start_time = models.DateTimeField("Время начала")
    end_time = models.DateTimeField("Время конца")
    game_set_price = models.IntegerField("Цена в рублях за час")
    hall_price = models.IntegerField("Цена за 1 час брони на 1 человека")

    id_order = models.ForeignKey("Order", on_delete=models.SET_NULL, null=True)
    id_hall = models.ForeignKey("Hall", on_delete=models.SET_NULL, null=True)
    id_game_set = models.ForeignKey("Game_set", on_delete=models.SET_NULL, null=True)

    
