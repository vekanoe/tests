import uuid
from dateutil.relativedelta import relativedelta

from django.db import models
from django.utils import timezone


class Position(models.Model):
    """ Должность """

    title = models.CharField('Наименование', max_length=250, unique=True)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.title


class Department(models.Model):
    """ Отдел """

    title = models.CharField('Наименование', max_length=250, unique=True)
    chief = models.OneToOneField('Employee', verbose_name='Директор', on_delete=models.PROTECT,
                                 related_name='+', unique=True)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.title

    @property
    def employees_count(self):
        return self.employees.count()

    @property
    def total_salary(self):
        return self.employees.aggregate(models.Sum('salary'))['salary__sum']

    def save(self, **kwargs):
        super().save(**kwargs)

        # директор отдела автоматически становится сотрудником данного отдела
        if self.chief.department != self:
            self.chief.department = self
            self.chief.save()


def get_photo(instance, filename):
    return "photos/{}-{}.{}".format(instance.pk or 0, uuid.uuid4(), filename.split('.')[-1])


class Employee(models.Model):
    """ Сотрудник """

    last_name = models.CharField('Фамилия', max_length=250, db_index=True)
    first_name = models.CharField('Имя', max_length=250)
    patronymic = models.CharField('Отчество', max_length=250)

    photo = models.ImageField('Фото', upload_to=get_photo, blank=True, null=True)
    salary = models.DecimalField('Оклад', max_digits=9, decimal_places=2)
    birth_date = models.DateField('Дата рождения')

    position = models.ForeignKey(Position, verbose_name='Должность', on_delete=models.PROTECT)
    department = models.ForeignKey(Department, verbose_name='Отдел', on_delete=models.PROTECT,
                                   related_name='employees', blank=True, null=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.fio} - {self.department}'

    @property
    def fio(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    @property
    def age(self):
        return relativedelta(timezone.localdate(timezone.now()), self.birth_date).years
