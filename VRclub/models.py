from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    class Role(models.IntegerChoices):
        undefined = 0
        employee = 1
        client = 2

    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, null=True, blank=True)
    role = models.IntegerField("Роль", choices=Role, default=Role.undefined)

    def __str__(self):
        return self.user.username if self.user else f"Profile {self.id}"
    
@receiver(post_save, sender=User)
def on_user_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance, role=Profile.Role.undefined)


class Genre(models.Model):
    name = models.TextField("Название")
    description = models.TextField("Общее описание")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Game(models.Model):
    name = models.TextField("Название")
    description = models.TextField("Общее описание")
    poster = models.ImageField("Постер")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"


class GenreInGame:
    id_genre = models.ForeignKey("Genre", on_delete=models.SET_NULL, null=True)
    id_game = models.ForeignKey("Game", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Жанры в игре"
        verbose_name_plural = "Жанры в играх"

class GameSet:
    name = models.TextField("Название")
    description = models.TextField("Описание")
    price_per_hour = models.IntegerField("Цена в рублях за час")


    class Meta:
        verbose_name = "Игровой набор"
        verbose_name_plural = "Игровые наборы"

class GameOnSet:
    id_game = models.ForeignKey("Game", on_delete=models.SET_NULL, null=True)
    id_gameSet = models.ForeignKey("GameSet", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Игры на игровом наборе"
        verbose_name_plural = "Игры на игровых набора"



class Hall:
    name = models.TextField("Наименование")
    description = models.TextField("Описание")
    capacity = models.IntegerField("Вместимость человек")
    price_per_hour = models.IntegerField("Цена за 1 час брони на 1 человека")


    class Meta:
        verbose_name = "Зал"
        verbose_name_plural = "Залы"

class Order:
    class Status(models.TextChoices):
        pending = "в работе", "в работе"
        executed = "завершен", "Завершен"
        cancelled = "отменён", "Отменён"

    total_amount = models.IntegerField("Общая стоимость заказа")
    status = models.TextField("Статус", choices=Status.choices, default=Status.pending)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        unique_together = ['id_order', 'id_hall', 'id_game_set']



class OrderItem:
    start_time = models.DateTimeField("Время начала")
    end_time = models.DateTimeField("Время конца")
    game_set_price = models.IntegerField("Цена в рублях за час")
    hall_price = models.IntegerField("Цена за 1 час брони на 1 человека")

    id_order = models.ForeignKey("Order", on_delete=models.SET_NULL, null=True)
    id_hall = models.ForeignKey("Hall", on_delete=models.SET_NULL, null=True)
    id_game_set = models.ForeignKey("GameSet", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Позиция"
        verbose_name_plural = "Позиции"
        unique_together = ['id_order', 'id_hall', 'id_game_set']


    
