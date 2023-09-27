from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    # for signals to work, override ready() function
    def ready(self):
        import accounts.signals

