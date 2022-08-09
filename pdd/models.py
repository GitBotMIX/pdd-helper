from django.db import models

class Pdd(models.Model):
    question = models.TextField('Вопросы')
    answer = models.TextField('Ответы')
    correctNumber = models.TextField('Цифра ответа')


    def __str__(self):
        return self.question
    class Meta:
        verbose_name = "Вопросы"
        verbose_name_plural = "Ответы"