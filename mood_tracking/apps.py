from django.apps import AppConfig


class MoodTrackingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mood_tracking'

class AuthenticationConfig(AppConfig):
    name = 'authentication'

    def ready(self):
        import authentication.signals
