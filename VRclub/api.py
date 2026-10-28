from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.middleware.csrf import get_token
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from VRclub.models import Genre
from VRclub.models import Profile
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


def _user_payload(user):
    profile, _ = Profile.objects.get_or_create(user=user)
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'role': profile.role,
    }


class ProfileViewSet(GenericViewSet):
    @action(detail=False, methods=['get'], url_path='csrf')
    @method_decorator(ensure_csrf_cookie)
    def csrf(self, request):
        return Response({'csrfToken': get_token(request)})

    @action(detail=False, methods=['get'], url_path='me')
    @method_decorator(ensure_csrf_cookie)
    def get_me(self, request):
        if not request.user.is_authenticated:
            return Response({'user': None})
        return Response({'user': _user_payload(request.user)})

    @action(detail=False, methods=['post'], url_path='login')
    @method_decorator(ensure_csrf_cookie)
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            return Response({'detail': 'Неверный логин или пароль'}, status=status.HTTP_400_BAD_REQUEST)
        django_login(request, user)
        return Response({'user': _user_payload(user)})

    @action(detail=False, methods=['post'], url_path='logout')
    @method_decorator(ensure_csrf_cookie)
    def logout(self, request):
        django_logout(request)
        return Response({'detail': 'Вы вышли из системы'})