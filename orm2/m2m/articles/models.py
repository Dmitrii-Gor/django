from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя тега')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Scopes(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scope')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scope', verbose_name='Тег')
    is_main = models.BooleanField()

    class Meta:
        verbose_name = 'Тематика статьи'