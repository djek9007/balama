
from django.db import models

# Create your models here.
from balama import settings
from catalog.models import Language
from publishingHouse.models import PublishingHouse, Subject, ClassRoom, YearPublising



class Alternative(models.Model):
    """Модель выбора алтернативных учебников"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publishingHouse = models.ForeignKey(PublishingHouse, verbose_name='Издательство', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, verbose_name='Предмет', on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom, verbose_name='Класс', on_delete=models.CASCADE)
    yearPublishing = models.ForeignKey(YearPublising, verbose_name='Год издание', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, verbose_name='Язык', on_delete=models.CASCADE)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now=True,

    )
    published = models.BooleanField("Опубликовать?", default=True)


    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Выбранные учебники'
        verbose_name_plural = 'Выбранные учебники'