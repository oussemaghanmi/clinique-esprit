from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Create or reset default admin user"

    def handle(self, *args, **options):
        print(">>> RUNNING create_default_admin <<<")
        User = get_user_model()
        username = "admin"
        password = "Admin@Clinic2026"
        email = "admin@example.com"

        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                "email": email,
                "is_staff": True,
                "is_superuser": True,
            },
        )

        if not created:
            user.set_password(password)
            user.is_staff = True
            user.is_superuser = True
            user.email = email
            user.save()
            self.stdout.write(self.style.SUCCESS("Superuser 'admin' password reset."))
        else:
            self.stdout.write(self.style.SUCCESS("Superuser 'admin' created."))
