# Generated by Django 2.2.8 on 2020-02-26 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_roleinfo_agreement_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='did',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
