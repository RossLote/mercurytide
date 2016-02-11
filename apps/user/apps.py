from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'
    verbose_name = 'User'

    def ready(self):
        from . import receivers
