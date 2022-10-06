from django.db import models


class StatusIssue(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=20,
        null=False,
        blank=False
    )

    def __str__(self) -> str:
        return f'{self.title}'


class TypeIssue(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=20,
        null=False,
        blank=False
    )

    def __str__(self) -> str:
        return f'{self.title}'


class Issue(models.Model):
    title = models.CharField(
        verbose_name='Краткое описание',
        max_length=100,
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name='Полное описание',
        max_length=800,
        default=''
    )
    status = models.ForeignKey(
        to='issuetracker.StatusIssue',
        related_name='statuses',
        on_delete=models.RESTRICT,
        verbose_name='Статус'
    )
    type_issue = models.ForeignKey(
        to='issuetracker.TypeIssue',
        related_name='types',
        on_delete=models.RESTRICT,
        verbose_name='Тип'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания',
    )
    updateted_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Время обновления'
    )

    def __str__(self) -> str:
        return f'{self.title}'