from django.db import models


class Course(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Курс", help_text="Укажите курс"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание", blank=True, null=True
    )
    image = models.ImageField(
        upload_to="materials/media",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Добавьте картинку",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Урок", help_text="Укажите урок"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        help_text="Выберите курс",
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание", blank=True, null=True
    )
    image = models.ImageField(
        upload_to="materials/media",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Добавьте картинку к уроку",
    )
    url = models.CharField(
        max_length=200,
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
