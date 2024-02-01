from django.db import models


class Coin(models.Model):
    # Задание №1
    # Создайте модель для запоминания бросков монеты: орёл или решка.
    # Также запоминайте время броска
    side = models.CharField(max_length=10)
    throw_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Coin is on side {self.side} at {self.throw_time}'

    # Задание №2
    # Доработаем задачу 1. Добавьте статический метод для статистики по n последним броскам монеты.
    # Метод должен возвращать словарь с парой ключей-значений, для орла и для решки.
    @staticmethod
    def get_statistics(throw_number):
        coins = Coin.objects.all()[:throw_number]
        coins_dict = {
            'Орел': [],
            'Решка': []
        }
        for coin in coins:
            if coin.side == 'Орел':
                coins_dict['Орел'].append(coin.throw_time)
            else:
                coins_dict['Решка'].append(coin.throw_time)
        return coins_dict

# Задание №3
# Создайте модель Автор. Модель должна содержать
# следующие поля:
# ○ имя до 100 символов
# ○ фамилия до 100 символов
# ○ почта
# ○ биография
# ○ день рождения
# Дополнительно создай пользовательское поле “полное имя”, которое возвращает имя и фамилию.


class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    def __str__(self):
        return f'Author: {self.name} {self.last_name}, birthday: {self.birthday}'

    def get_full_name(self):
        return f'{self.name} {self.last_name}'

# Задание №4
# Создайте модель Статья (публикация). Авторы из прошлой задачи могут
# писать статьи. У статьи может быть только один автор. У статьи должны быть
# следующие обязательные поля:
# ○ заголовок статьи с максимальной длиной 200 символов
# ○ содержание статьи
# ○ дата публикации статьи
# ○ автор статьи с удалением связанных объектов при удалении автора
# ○ категория статьи с максимальной длиной 100 символов
# ○ количество просмотров статьи со значением по умолчанию 0
# ○ флаг, указывающий, опубликована ли статья со значением по умолчанию False

class Post(models.Model):
    title = models.CharField(max_length=200)
    # post_category = models.CharField(max_length=100)
    content = models.TextField()
    # publishing_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'Post: {self.title}, Author: {self.author}, views: {self.views}'
    
    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:12])}...'
