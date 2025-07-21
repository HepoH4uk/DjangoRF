from django.db import models


class Course(models.Model):

    name = models.CharField(
        max_length=30,
        verbose_name="Название",
        help_text="Укажите название",
    )

    description = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Добавьте описание"
    )

    preview = models.ImageField(
        upload_to="lessons/picture",
        blank=True,
        null=True,
        verbose_name="Картинка",
        help_text="Добавьте картинку",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):

    name = models.CharField(
        max_length=30,

        verbose_name="Название",
        help_text="Укажите название",
    )

    description = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Добавьте описание"
    )

    preview = models.ImageField(
        upload_to="lessons/picture",
        blank=True,
        null=True,
        verbose_name="Картинка",
        help_text="Добавьте картинку",
    )

    video_url = models.URLField(
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео",
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lessons",
        verbose_name="Курс",
        help_text="Выберите курс",
    )


    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


    def __str__(self):
        return self.name
