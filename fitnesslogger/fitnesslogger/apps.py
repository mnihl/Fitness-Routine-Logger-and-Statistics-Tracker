from django.apps import AppConfig

class FitnessloggerConfig(AppConfig):
    name = 'fitnesslogger'

    def ready(self):
        import fitnesslogger.signals