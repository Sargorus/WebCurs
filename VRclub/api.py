from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from VRclub.models import Genre
from VRclub.models import Game
from VRclub.models import GenreInGame
from VRclub.models import GameSet
from VRclub.models import GameOnSet
from VRclub.models import Hall
from VRclub.models import Order
from VRclub.models import OrderItem
from VRclub.serializers import GenreSerializer
from VRclub.serializers import GameSerializer
from VRclub.serializers import GenreInGameSerializer
from VRclub.serializers import GameSetSerializer
from VRclub.serializers import GameOnSetSerializer
from VRclub.serializers import HallSerializer
from VRclub.serializers import OrderSerializer
from VRclub.serializers import OrderItemSerializer


class GenreViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GameViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GenreInGameViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = GenreInGame.objects.all()
    serializer_class = GenreInGameSerializer


class GameSetViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = GameSet.objects.all()
    serializer_class = GameSetSerializer


class GameOnSetViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = GameOnSet.objects.all()
    serializer_class = GameOnSetSerializer


class HallViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer


class OrderViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer