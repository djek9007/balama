from django.db import models

# Create your models here.
# Create your models here.
from catalog.models import Subject, ClassRoom, Language


class YearPublising(models.Model):
    name = models.CharField('Год издание', max_length=100)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now=True,
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Год издание"
        verbose_name_plural = "Год издание"


class PublishingHouse(models.Model):
    name = models.CharField('Издательство', max_length=100)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now=True,
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательство"


class TextBook(models.Model):
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
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    cover = models.ImageField(verbose_name='Обложка', upload_to='uploads/book/%Y/%m/%d/', blank=True, null=True)
    link = models.CharField(verbose_name='Внешняя ссылка на учебник', blank=True, null=True, max_length=255)
    file = models.FileField(upload_to='uploads/book/file/%Y/%m/%d/', verbose_name='Учебник для прикрепление', blank=True, null=True, help_text="загружать только pdf")

    def __str__(self):
        return self.publishingHouse.name

    class Meta:
        verbose_name = "Учебники"
        verbose_name_plural = "Учебники"