from django.db import models



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
        verbose_name='Статус',
        default='New'
    )
    type_issue = models.ManyToManyField(
        to='issuetracker.TypeIssue',
        related_name='issues',
        verbose_name='Тип',
        blank=True,
        default='Task'
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