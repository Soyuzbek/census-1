# Generated by Django 2.2.8 on 2020-02-18 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200218_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='каттоо бөлүмү'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='plot',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='каттоо участогу'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sector',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='инструктордук участок'),
        ),
    ]