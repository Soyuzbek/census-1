# Generated by Django 2.2.5 on 2020-01-14 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(upload_to='users/img', verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.CharField(choices=[('enum', 'Каттоочу'), ('ins', 'Инструктор'), ('cor', 'Координатор')], default=('cor', 'Координатор'), max_length=50, verbose_name='role'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sector',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15')], default=1, verbose_name='Instructor sector'),
        ),
    ]