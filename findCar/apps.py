from django.apps import AppConfig




class FindcarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'findCar'

    def ready(self):
        from findCar.signals import start_scheduler_on_startup
        start_scheduler_on_startup()
