from django.db import models

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class Project(models.Model):
    description = models.TextField(verbose_name='Описание')
    status = models.CharField(max_length=20, choices= STATUS_CHOICES, verbose_name='Статус', default=STATUS_CHOICES[0][0])
    create_add = models.DateField(null=True, blank= True, verbose_name='дата создание')

    def __str__(self):
        return f"{self.description}. {self.status} : {self.create_add}"

    class Meta:
        db_table = 'projects'
        verbose_name = 'проекты'
        verbose_name_plural = 'проект'