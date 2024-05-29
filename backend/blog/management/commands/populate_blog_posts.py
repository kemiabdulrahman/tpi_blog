from django.core.management.base import BaseCommand
from blog.tests.factories import PostFactory 

class Command(BaseCommand):
    help = 'Populate the database with agent using factory_boy'

    def handle(self, *args, **kwargs):
        num_preferences = 40  

        for _ in range(num_preferences):
            post = PostFactory.create()
            self.stdout.write(self.style.SUCCESS(f'Created post: {post.title}'))

        self.stdout.write(self.style.SUCCESS('Database population completed'))

