from django.core.management.base import BaseCommand
from lesson1_app.models import Author
import datetime


class Command(BaseCommand):
    help = "Generate fake authors"

    # def add_arguments(self, parser):
    #     parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        # count = kwargs.get('count')
        for i in range(1, 11):
            author = Author(name=f'Name{i}', last_name=f'Last name{i}', email=f'mail{i}@mail.ru',
                            biography=f'biography {i}', birthday=datetime.date(1980, 1, 1))
            author.save()
