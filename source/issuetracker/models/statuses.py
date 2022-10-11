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