from django.core.management.base import BaseCommand
from lesson1_app.models import Post, Author
from datetime import datetime


class Command(BaseCommand):
    help = "Generate fake posts"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of post to create per author')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        authors = Author.objects.all()
        for author in authors:
            for i in range(1, count + 1):
                post = Post(
                    title=f'Title {i}',
                    content=f'Content {i}',
                    author=author,
                    is_published=1
                )
                
                self.stdout.write(self.style.SUCCESS(f'Created post: {post}'))
                post.save()