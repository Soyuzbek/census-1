# Generated by Django 2.2.8 on 2020-03-05 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0039_auto_20200302_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='stat',
            field=models.CharField(max_length=255, null=True, verbose_name='stat'),
        ),
    ]