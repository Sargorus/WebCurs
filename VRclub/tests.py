from django.test import TestCase
from rest_framework.test import APIClient
from model_bakery import baker

from VRclub.models import Genre
from VRclub.models import Game
from VRclub.models import GenreInGame
from VRclub.models import GameSet
from VRclub.models import GameOnSet
from VRclub.models import Hall
from VRclub.models import Order
from VRclub.models import OrderItem


class GenreViewsetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        genre = baker.make(Genre)
        r = self.client.get('/api/genres/')
        data = r.json()
        assert len(data) == 1
        assert data[0]['name'] == genre.name

    def test_create(self):
        r = self.client.post('/api/genres/', {'name': 'test2', 'description': 'test2'})

        new_id = r.json()['id']
        assert Genre.objects.count() == 1
        assert Genre.objects.get(id=new_id).name == 'test2'

    def test_delete(self):
        genres = baker.make(Genre, 10)
        r = self.client.get('/api/genres/')
        data = r.json()
        assert len(data) == 10

        genre_id_to_delete = genres[3].id
        self.client.delete(f'/api/genres/{genre_id_to_delete}/')

        r = self.client.get('/api/genres/')
        data = r.json()
        assert len(data) == 9

        assert genre_id_to_delete not in [i['id'] for i in data]

    def test_update(self):
        genres = baker.make(Genre, 10)
        genre = genres[3]

        r = self.client.get(f'/api/genres/{genre.id}/')
        data = r.json()
        assert data['name'] == genre.name

        r = self.client.put(f'/api/genres/{genre.id}/', {'name': 'test2', 'description': 'test2'})
        assert r.status_code == 200
        r = self.client.get(f'/api/genres/{genre.id}/')
        data = r.json()
        assert data['name'] == 'test2'

        genre.refresh_from_db()
        assert data['name'] == genre.name


class GameViewsetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        game = baker.make(Game)
        r = self.client.get('/api/games/')
        data = r.json()
        assert len(data) == 1
        assert data[0]['name'] == game.name

    def test_create(self):
        r = self.client.post('/api/games/', {'name': 'test2', 'description': 'test2'})

        new_id = r.json()['id']
        assert Game.objects.count() == 1
        assert Game.objects.get(id=new_id).name == 'test2'

    def test_delete(self):
        games = baker.make(Game, 10)
        r = self.client.get('/api/games/')
        data = r.json()
        assert len(data) == 10

        game_id_to_delete = games[3].id
        self.client.delete(f'/api/games/{game_id_to_delete}/')

        r = self.client.get('/api/games/')
        data = r.json()
        assert len(data) == 9

        assert game_id_to_delete not in [i['id'] for i in data]

    def test_update(self):
        games = baker.make(Game, 10)
        game = games[3]

        r = self.client.get(f'/api/games/{game.id}/')
        data = r.json()
        assert data['name'] == game.name

        r = self.client.put(f'/api/games/{game.id}/', {'name': 'test2', 'description': 'test2'})
        assert r.status_code == 200
        r = self.client.get(f'/api/games/{game.id}/')
        data = r.json()
        assert data['name'] == 'test2'

        game.refresh_from_db()
        assert data['name'] == game.name


class GenreInGameViewsetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        relation = baker.make(GenreInGame)
        r = self.client.get('/api/genre-in-games/')
        data = r.json()
        assert len(data) == 1
        assert data[0]['id'] == relation.id

    def test_create(self):
        genre = baker.make(Genre)
        game = baker.make(Game)
        r = self.client.post('/api/genre-in-games/', {'id_genre': genre.id, 'id_game': game.id})

        new_id = r.json()['id']
        assert GenreInGame.objects.count() == 1
        assert GenreInGame.objects.get(id=new_id).id_genre_id == genre.id

    def test_delete(self):
        relations = baker.make(GenreInGame, 10)
        r = self.client.get('/api/genre-in-games/')
        data = r.json()
        assert len(data) == 10

        relation_id_to_delete = relations[3].id
        self.client.delete(f'/api/genre-in-games/{relation_id_to_delete}/')

        r = self.client.get('/api/genre-in-games/')
        data = r.json()
        assert len(data) == 9

        assert relation_id_to_delete not in [i['id'] for i in data]

    def test_update(self):
        genre = baker.make(Genre)
        game = baker.make(Game)
        relation = baker.make(GenreInGame, id_genre=genre, id_game=game)

        r = self.client.get(f'/api/genre-in-games/{relation.id}/')
        data = r.json()
        assert data['id'] == relation.id

        r = self.client.put(f'/api/genre-in-games/{relation.id}/', {'id_genre': genre.id, 'id_game': game.id})
        assert r.status_code == 200
        r = self.client.get(f'/api/genre-in-games/{relation.id}/')
        data = r.json()
        assert data['id_game'] == game.id

        relation.refresh_from_db()
        assert data['id_game'] == relation.id_game_id


class GameSetViewsetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        game_set = baker.make(GameSet)
        r = self.client.get('/api/game-sets/')
        data = r.json()
        assert len(data) == 1
        assert data[0]['name'] == game_set.name

    def test_create(self):
        r = self.client.post('/api/game-sets/', {'name': 'test2', 'description': 'test2', 'price_per_hour': 500})

        new_id = r.json()['id']
        assert GameSet.objects.count() == 1
        assert GameSet.objects.get(id=new_id).name == 'test2'

    def test_delete(self):
        game_sets = baker.make(GameSet, 10)
        r = self.client.get('/api/game-sets/')
        data = r.json()
        assert len(data) == 10

        game_set_id_to_delete = game_sets[3].id
        self.client.delete(f'/api/game-sets/{game_set_id_to_delete}/')

        r = self.client.get('/api/game-sets/')
        data = r.json()
        assert len(data) == 9

        assert game_set_id_to_delete not in [i['id'] for i in data]

    def test_update(self):
        game_sets = baker.make(GameSet, 10)
        game_set = game_sets[3]

        r = self.client.get(f'/api/game-sets/{game_set.id}/')
        data = r.json()
        assert data['name'] == game_set.name

        r = self.client.put(f'/api/game-sets/{game_set.id}/', {'name': 'test2', 'description': 'test2', 'price_per_hour': 500})
        assert r.status_code == 200
        r = self.client.get(f'/api/game-sets/{game_set.id}/')
        data = r.json()
        assert data['name'] == 'test2'

        game_set.refresh_from_db()
        assert data['name'] == game_set.name


class GameOnSetViewsetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        relation = baker.make(GameOnSet)
        r = self.client.get('/api/game-on-sets/')
        data = r.json()
        assert len(data) == 1
        assert data[0]['id'] == relation.id

    def test_create(self):
        game = baker.make(Game)
        game_set = baker.make(GameSet)
        r = self.client.post('/api/game-on-sets/', {'id_game': game.id, 'id_game_set': game_set.id})

        new_id = r.json()['id']
        assert GameOnSet.objects.count() == 1
        assert GameOnSet.objects.get(id=new_id).id_game_id == game.id

    def test_delete(self):
        relations = baker.make(GameOnSet, 10)
        r = self.client.get('/api/game-on-sets/')
        data = r.json()
        assert len(data) == 10

        relation_id_to_delete = relations[3].id
        self.client.delete(f'/api/game-on-sets/{relation_id_to_delete}/')

        r = self.client.get('/api/game-on-sets/')
        data = r.json()
        assert len(data) == 9

        assert relation_id_to_delete not in [i['id'] for i in data]

    def test_update(self):
        game = baker.make(Game)
        game_set = baker.make(GameSet)
        relation = baker.make(GameOnSet, id_game=game, id_game_set=game_set)

        r = self.client.get(f'/api/game-on-sets/{relation.id}/')
        data = r.json()
        assert data['id'] == relation.id

        r = self.client.put(f'/api/game-on-sets/{relation.id}/', {'id_game': game.id, 'id_game_set': game_set.id})
        assert r.status_code == 200
        r = self.client.get(f'/api/game-on-sets/{relation.id}/')
        data = r.json()
        assert data['id_game_set'] == game_set.id

        relation.refresh_from_db()
        assert data['id_game_set'] == relation.id_game_set_id


class HallViewsetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        hall = baker.make(Hall)
        r = self.client.get('/api/halls/')
        data = r.json()
        assert len(data) == 1
        assert data[0]['name'] == hall.name

    def test_create(self):
        r = self.client.post('/api/halls/', {'name': 'test2', 'description': 'test2', 'capacity': 10, 'price_per_hour': 500})

        new_id = r.json()['id']
        assert Hall.objects.count() == 1
        assert Hall.objects.get(id=new_id).name == 'test2'

    def test_delete(self):
        halls = baker.make(Hall, 10)
        r = self.client.get('/api/halls/')
        data = r.json()
        assert len(data) == 10

        hall_id_to_delete = halls[3].id
        self.client.delete(f'/api/halls/{hall_id_to_delete}/')

        r = self.client.get('/api/halls/')
        data = r.json()
        assert len(data) == 9

        assert hall_id_to_delete not in [i['id'] for i in data]

    def test_update(self):
        halls = baker.make(Hall, 10)
        hall = halls[3]

        r = self.client.get(f'/api/halls/{hall.id}/')
        data = r.json()
        assert data['name'] == hall.name

        r = self.client.put(f'/api/halls/{hall.id}/', {'name': 'test2', 'description': 'test2', 'capacity': 10, 'price_per_hour': 500})
        assert r.status_code == 200
        r = self.client.get(f'/api/halls/{hall.id}/')
        data = r.json()
        assert data['name'] == 'test2'

        hall.refresh_from_db()
        assert data['name'] == hall.name


class OrderViewsetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        order = baker.make(Order)
        r = self.client.get('/api/orders/')
        data = r.json()
        assert len(data) == 1
        assert data[0]['id'] == order.id

    def test_create(self):
        r = self.client.post('/api/orders/', {'total_amount': 1000, 'status': 'в работе'})

        new_id = r.json()['id']
        assert Order.objects.count() == 1
        assert Order.objects.get(id=new_id).total_amount == 1000

    def test_delete(self):
        orders = baker.make(Order, 10)
        r = self.client.get('/api/orders/')
        data = r.json()
        assert len(data) == 10

        order_id_to_delete = orders[3].id
        self.client.delete(f'/api/orders/{order_id_to_delete}/')

        r = self.client.get('/api/orders/')
        data = r.json()
        assert len(data) == 9

        assert order_id_to_delete not in [i['id'] for i in data]

    def test_update(self):
        orders = baker.make(Order, 10)
        order = orders[3]

        r = self.client.get(f'/api/orders/{order.id}/')
        data = r.json()
        assert data['id'] == order.id

        r = self.client.put(f'/api/orders/{order.id}/', {'total_amount': 2000, 'status': 'завершен'})
        assert r.status_code == 200
        r = self.client.get(f'/api/orders/{order.id}/')
        data = r.json()
        assert data['total_amount'] == 2000

        order.refresh_from_db()
        assert data['total_amount'] == order.total_amount


class OrderItemViewsetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        order_item = baker.make(OrderItem)
        r = self.client.get('/api/order-items/')
        data = r.json()
        assert len(data) == 1
        assert data[0]['id'] == order_item.id

    def test_create(self):
        r = self.client.post('/api/order-items/', {
            'start_time': '2026-01-01T10:00:00Z',
            'end_time': '2026-01-01T11:00:00Z',
            'game_set_price': 500,
            'hall_price': 300,
        })

        new_id = r.json()['id']
        assert OrderItem.objects.count() == 1
        assert OrderItem.objects.get(id=new_id).game_set_price == 500

    def test_delete(self):
        order_items = baker.make(OrderItem, 10)
        r = self.client.get('/api/order-items/')
        data = r.json()
        assert len(data) == 10

        order_item_id_to_delete = order_items[3].id
        self.client.delete(f'/api/order-items/{order_item_id_to_delete}/')

        r = self.client.get('/api/order-items/')
        data = r.json()
        assert len(data) == 9

        assert order_item_id_to_delete not in [i['id'] for i in data]

    def test_update(self):
        order = baker.make(Order)
        hall = baker.make(Hall)
        game_set = baker.make(GameSet)
        order_items = baker.make(OrderItem, 10)
        order_item = order_items[3]

        r = self.client.get(f'/api/order-items/{order_item.id}/')
        data = r.json()
        assert data['id'] == order_item.id

        r = self.client.put(f'/api/order-items/{order_item.id}/', {
            'start_time': '2026-01-01T10:00:00Z',
            'end_time': '2026-01-01T11:00:00Z',
            'game_set_price': 700,
            'hall_price': 300,
            'id_order': order.id,
            'id_hall': hall.id,
            'id_game_set': game_set.id,
        })
        assert r.status_code == 200
        r = self.client.get(f'/api/order-items/{order_item.id}/')
        data = r.json()
        assert data['game_set_price'] == 700

        order_item.refresh_from_db()
        assert data['game_set_price'] == order_item.game_set_price