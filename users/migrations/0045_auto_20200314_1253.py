# Generated by Django 2.2.8 on 2020-03-14 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0044_auto_20200314_1250'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='employee',
            unique_together={('district', 'agreement'), ('serial', 'passport_num')},
        ),
    ]