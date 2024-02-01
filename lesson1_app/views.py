from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from random import randint, choice
from . models import Coin, Author, Post
from .forms import GameTypeForm, AuthorAddForm, PostAddFormWidget
import logging
# Create your views here.

logger = logging.getLogger(__name__)


# def index(request):
#     logger.info('Index page accessed')
#     return HttpResponse("Hello, world!")

# Задание №5
# � Создайте новое приложение. Подключите его к проекту. В
# приложении должно быть три простых представления,
# возвращающих HTTP ответ:
# � Орёл или решка
# � Значение одной из шести граней игрального кубика
# � Случайное число от 0 до 100
# � Пропишите маршруты

# Семинар 3
# Задание №3
# Доработаем задачу 7 из урока 1, где бросали монетку, игральную кость и генерировали случайное число.
# Маршруты могут принимать целое число - количество бросков.
# Представления создают список с результатами бросков и передают его в контекст шаблона.
# Необходимо создать универсальный шаблон для вывода результатов любого из трёх представлений.

def heads_and_tails(request, throws_number):
    result_list = []
    for i in range(throws_number):
        result = choice(['Орел', 'Решка'])
        result_list.append(f'Coin throw {i+1}: side - {result}')
        logger.info(f'Coin side: {result}')
    #     coin = Coin(side=result)
    #     coin.save()
    # coins_dict = Coin.get_statistics(5)
    context = {
        'title': 'Heads and tails',
        'result': result_list,
    }
    return render(request, template_name='lesson1_app/base_for_task3.html', context=context)


def dice(request, throws_number):
    result_list = []
    for i in range(throws_number):
        dice_side = randint(1, 6)
        result_list.append(f'Dice throw {i+1}: {dice_side}')
        logger.info(f'Dice side: {dice_side}')

    context = {
        'title': 'Dice',
        'result': result_list,
    }
    return render(request, template_name='lesson1_app/base_for_task3.html', context=context)


def random_number(request, throws_number):
    result_list = []
    for i in range(throws_number):
        random_number = randint(0, 100)
        result_list.append(f'random number {i+1}: {random_number}')
        logger.info(f'Random number: {random_number}')
    context = {
        'title': 'Random number',
        'result': result_list,
    }
    return render(request, template_name='lesson1_app/base_for_task3.html', context=context)


def authors_view(request):
    authors = Author.objects.all()
    result = '<br>'.join([str(author) for author in authors])

    return (HttpResponse(result))


def posts_view(request):
    posts = Post.objects.all()
    result = '<br>'.join([str(post) for post in posts])

    return (HttpResponse(result))


# Семинар 3
# Задание №1
# Изменяем задачу 8 из семинара 1 с выводом двух html страниц:
# главной и о себе.
# Перенесите вёрстку в шаблоны.
# Представления должны пробрасывать полезную информацию в
# шаблон через контекст.

def index(request):
    logger.info('Index page accessed')
    context = {
        'title': 'main page'
    }
    return render(request, template_name='lesson1_app/index.html', context=context)


def about(request):
    logger.info('About page accessed')
    context = {
        'name': 'Oksana'
    }
    return render(request, template_name='lesson1_app/about.html', context=context)


# Задание №4
# Доработаем задачи из прошлого семинара по созданию
# моделей автора, статьи и комментария.
# Создайте шаблон для вывода всех статей автора в виде
# списка заголовков.
# ○ Если статья опубликована, заголовок должен быть
# ссылкой на статью.
# ○ Если не опубликована, без ссылки.
# Не забываем про код представления с запросом к базе
# данных и маршруты.
def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')
    return render(request, template_name='lesson1_app/author_posts.html', context={'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.views += 1
    post.save()
    return render(request, 'lesson1_app/post_full.html', {'post': post})


# Доработаем задачу 1. Создайте представление, которое выводит форму выбора.
# В зависимости переданных значений представление вызывает одно из трёх представлений,
# созданных на прошлом семинаре (если данные прошли проверку, конечно же).
def choose_game(request):
    if request.method == 'POST':
        form = GameTypeForm(request.POST)
        if form.is_valid():
            game_type = form.cleaned_data['game_type']
            throws_number = form.cleaned_data['throws_number']
            logger.info(f'Получили {game_type=}, {throws_number=}.')
            if game_type == 'C':
                return heads_and_tails(request, throws_number)
            elif game_type == 'D':
                return dice(request, throws_number)
            else:
                return random_number(request, throws_number)

    else:
        form = GameTypeForm()
    return render(request, 'lesson1_app/games.html', {'form': form})


def author_add(request):
    if request.method == 'POST':
        form = AuthorAddForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            biography = form.cleaned_data['biography']
            birthday = form.cleaned_data['birthday']
            logger.info(f'Получили {name=}')
            author = Author(name=name, last_name=last_name, email=email, biography=biography, birthday=birthday)
            author.save()
            message = 'Автор сохранён'
    else:
        form = AuthorAddForm()
        message = 'Заполните форму'
    return render(request, 'lesson1_app/author_form.html', {'form': form, 'message': message})

def post_add(request):
    if request.method == 'POST':
        form = PostAddFormWidget(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            # publishing_date = form.cleaned_data['publishing_date']
            author = form.cleaned_data['author']
            is_published = form.cleaned_data['is_published']
            logger.info(f'Получили {title=}')
            post = Post(title=title, content=content, author=author, is_published=is_published)
            post.save()
            message = 'Статья сохранена'
    else:
        form = PostAddFormWidget()
        message = 'Заполните форму'
    return render(request, 'lesson1_app/post_form.html', {'form': form, 'message': message})