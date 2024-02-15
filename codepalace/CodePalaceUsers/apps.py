from django.apps import AppConfig


class CodepalaceusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CodePalaceUsers'

    def ready(self):
        import CodePalaceUsers.signals
