# Generated by Django 2.2.8 on 2020-02-26 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_auto_20200226_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='roleinfo',
            name='agreement_day',
            field=models.DateField(blank=True, null=True),
        ),
    ]
