from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Region(models.Model):
    """Модель таблицы области"""
    name = models.CharField(_('Область/город'), max_length=100)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now=True,
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.name



    class Meta:
        verbose_name = "Область"
        verbose_name_plural = "Области"


class District(models.Model):
    """Модель таблицы Района"""
    region = models.ForeignKey(Region, verbose_name='Область/город', on_delete=models.CASCADE)
    name = models.CharField(_('Район'), max_length=100)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now=True,
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"


class Locality(models.Model):
    """Модель таблицы населенного пункта"""
    region = models.ForeignKey(Region, verbose_name='Область/город', on_delete=models.CASCADE)
    district = models.ForeignKey(District, verbose_name='Район', on_delete=models.CASCADE, related_name='district_locality')
    name = models.CharField(_('Населенный пункт'), max_length=100)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now=True,
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Населенный пункт"
        verbose_name_plural = "Населенные пункты"

class TerritorialAffiliation(models.Model):
    """Модель таблицы территориальная принадлежность город село"""

    name = models.CharField(_('Вид территориальной принадлежности'), max_length=100, unique=True)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now=True,
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Территориральная принадлежность"
        verbose_name_plural = "Территориальные принадлежности"

class Language(models.Model):
    """Таблица языков"""
    name = models.CharField(_('Язык'), max_length=100)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now=True,
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.name



    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"

class Subject(models.Model):
    """Модель таблицы предметов Геометрия, математика итд"""
    language = models.ForeignKey(Language, verbose_name='Язык обучение', on_delete=models.CASCADE)
    name = models.CharField(_('Наименование предмета'), max_length=100)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now=True,
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"


class ClassRoom(models.Model):
    """Модель таблицы класса от 1 до 11 класс"""
    name = models.CharField(_('Класс'), max_length=100)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now=True,
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Класс"
        verbose_name_plural = "Классы"

