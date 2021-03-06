# Generated by Django 2.2.5 on 2020-01-29 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200128_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='center',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='райондун борбору'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_badge_printed',
            field=models.BooleanField(default=False, verbose_name='бейджик басып чыгарылдыбы?'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_badge_returned',
            field=models.BooleanField(default=False, verbose_name='бейджик кайтарылдыбы?'),
        ),
    ]
