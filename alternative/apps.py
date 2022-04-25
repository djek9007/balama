from django.apps import AppConfig


class AlternativeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'alternative'
    verbose_name = 'Выбранные учебники'
    verbose_name_plural = 'Выбранные учебники'
