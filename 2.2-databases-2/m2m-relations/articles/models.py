from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField('Tag', through='Scope', related_name='articles')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):

    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


    def __str__(self):
        return self.name


class Scope(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья', related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Раздел', related_name='scopes')
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        verbose_name = 'Раздел статей'
        verbose_name_plural = 'Разделы статьи'
        ordering = ['-is_main']
