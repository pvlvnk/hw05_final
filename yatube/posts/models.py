from core.models import CreatedModel
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import constraints

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок',
        help_text='Введите заголовок'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Уникальная строка',
        help_text='Введите уникальную строку'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите описание'
    )

    def __str__(self) -> str:
        return self.title


class Post(CreatedModel):
    text = models.TextField(
        verbose_name='Текст',
        help_text='Введите текст'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
        help_text='Введите дату публикации'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Группа',
        help_text='Введите название группы'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
        help_text='Введите автора'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        blank=True
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text[:15]


class Comment(CreatedModel):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост, к которому прикрепляется комментарий',
        help_text='Укажите пост'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        help_text='Введите автора',
    )
    text = models.TextField(
        verbose_name='Текст',
        help_text='Введите текст'
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:15]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Пользователь',
        help_text='Укажите подписчика'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
        help_text='Укажите автора'
    )

    class Meta:
        constraints = [
            constraints.UniqueConstraint(
                fields=['user', 'author'], name='follow_unique')
        ]

        def __str__(self):
            return self.user.username, self.author.username
