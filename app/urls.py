from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings

from VRclub.api import GenreViewSet
from VRclub.api import GameViewSet
from VRclub.api import GenreInGameViewSet
from VRclub.api import GameSetViewSet
from VRclub.api import GameOnSetViewSet
from VRclub.api import HallViewSet
from VRclub.api import OrderViewSet
from VRclub.api import OrderItemViewSet

router = DefaultRouter()
router.register('genres', GenreViewSet, 'genres')
router.register('games', GameViewSet, 'games')
router.register('genre-in-games', GenreInGameViewSet, 'genre-in-games')
router.register('game-sets', GameSetViewSet, 'game-sets')
router.register('game-on-sets', GameOnSetViewSet, 'game-on-sets')
router.register('halls', HallViewSet, 'halls')
router.register('orders', OrderViewSet, 'orders')
router.register('order-items', OrderItemViewSet, 'order-items')


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)