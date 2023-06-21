from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

# from django.shortcuts import get_object_or_404


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("del_users", type=int, nargs="+")

    def handle(self, *args, **options):
        User.objects.filter(pk__in=options.get("del_users")).filter(is_superuser=False).delete()

        # for del_user in options.get('del_users'):
        #     u = get_object_or_404(User, id=del_user)
