# myapp/factories.py
import factory
from factory import Faker
from factory.django import DjangoModelFactory
from blog.models import Post
from django.contrib.auth.models import User
"""
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Faker('user_name')
    email = Faker('email')
"""

class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = Faker('sentence', nb_words=6)
    content = Faker('paragraph', nb_sentences=3)
    # author = factory.SubFactory(UserFactory)

