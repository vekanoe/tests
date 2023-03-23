# Generated by Django 4.1.7 on 2023-03-22 20:16

import company.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(db_index=True, max_length=250, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=250, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=250, verbose_name='Отчество')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=company.models.get_photo, verbose_name='Фото')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Оклад')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employees', to='company.department', verbose_name='Отдел')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.position', verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='chief',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='company.employee', verbose_name='Директор'),
        ),
    ]