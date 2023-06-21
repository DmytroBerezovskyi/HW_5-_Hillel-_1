from django.core.management.base import BaseCommand
from faker import Faker

from django.contrib.auth.models import User

faker = Faker()


class Command(BaseCommand):
    def add_arguments(self, parser):
        # parser.add_argument('quan_users', type=int)
        parser.add_argument("quan_users", type=int, choices=range(1, 11))

    def handle(self, *args, **options):
        quant = options.get("quan_users")
        user = User.objects.bulk_create(
            User(username=faker.first_name(), email=faker.email(), password=faker.password()) for _ in range(quant)
        )
