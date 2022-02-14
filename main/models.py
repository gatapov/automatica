from django.db import models
from django.utils import timezone


class Employee(models.Model):
    name = models.CharField(default='', blank=False, max_length=10, verbose_name='Имя')
    phone = models.CharField(default='', blank=False, max_length=11, verbose_name='Телефон', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class Store(models.Model):
    name = models.CharField(default='', blank=False, max_length=100, verbose_name='Название')
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, verbose_name='Работник')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Visit(models.Model):
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата и время')
    store = models.ForeignKey(Store, on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, verbose_name='Сотрудник', blank=False)
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)

    def __str__(self):
        return f'Посещение магазина {self.store.name} - {self.date}'

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'
