from django.apps import AppConfig

class VelvetWalkAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'VelvetWalk_app'

    def ready(self):
        import VelvetWalk_app.signals 