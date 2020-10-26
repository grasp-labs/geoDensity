from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseCommand):
    """
    Create default administrators
    """

    def handle(self, *args, **options):
        User = get_user_model()
        for user in settings.ADMINS:
            username, email = user
            password = settings.ADMIN_INITIAL_PASSWORD
            try:
                User.objects.get(username=username)
            except ObjectDoesNotExist:
                print('Creating account for %s' % email)
                admin = User.objects.create_superuser(
                    email=email,
                    username=username,
                    password=password)
                admin.is_active = True
                admin.is_staff = True
                admin.is_admin = True
                admin.is_superuser = True
                admin.save()
