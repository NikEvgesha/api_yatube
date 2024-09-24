from django.contrib.auth import get_user_model
from django.db import models

from posts.constants import TITLE_STR_LIMIT, TEXT_STR_LIMIT


User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Slug"
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title[:TITLE_STR_LIMIT]


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='Изображение'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Группа'
    )

    class Meta:
        default_related_name = 'posts'

    def __str__(self):
        return self.text[:TEXT_STR_LIMIT]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Комментарии к посту'
    )
    text = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        default_related_name = 'comments'

    def __str__(self):
        return (f'{self.post} ({self.author.username}): '
                f'{self.text[:TEXT_STR_LIMIT]}')
