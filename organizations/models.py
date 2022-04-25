from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from balama import settings
from catalog.models import Region, District, Locality, TerritorialAffiliation, Language


class Organization(models.Model):
    """Модель таблицы организации"""
    region = models.ForeignKey(Region, verbose_name='Область', on_delete=models.CASCADE)
    district = models.ForeignKey(District, verbose_name='Район', on_delete=models.CASCADE)
    locality = models.ForeignKey(Locality, verbose_name='Населенный пункт', on_delete=models.CASCADE)
    territoriAlaffiliation = models.ForeignKey(TerritorialAffiliation, verbose_name='Территориральная принадлежность', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, verbose_name='Язык', on_delete=models.CASCADE)
    name = models.CharField(_('Наименование организации'), max_length=100,)

    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now=True,
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"


class MethodicalAssociation(models.Model):
    """Таблица методических объединении"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, verbose_name='Организация', on_delete=models.CASCADE)
    name = models.CharField(_('Наименование методического объединение'), max_length=200,)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now=True,
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Методические объединение"
        verbose_name_plural = "Методические объединение"


class MetodicalMember(models.Model):
    """Таблица членов методического объединение"""
    metodicalAssociation = models.ForeignKey(MethodicalAssociation, verbose_name='Наименование методического объединение', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='ФИО участника методического объединение', max_length=150)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now=True,
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.metodicalAssociation.name

    class Meta:
        verbose_name = "Члены методического объединение"
        verbose_name_plural = "Члены методического объединение"