# Generated by Django 2.2.8 on 2020-02-20 03:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200219_1457'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name': 'District', 'verbose_name_plural': 'Districts'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['-id'], 'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'Region', 'verbose_name_plural': 'Regions'},
        ),
        migrations.AlterModelOptions(
            name='territory',
            options={'ordering': ['code'], 'verbose_name': 'Territory', 'verbose_name_plural': 'Territories'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('can_print_badge', 'Can print a badge'), ('can_print_agreement', 'Can print an agreement')], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='district',
            name='center',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='center of district'),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=55, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='district',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Region', verbose_name='region'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='PIN',
            field=models.CharField(max_length=14, verbose_name='PIN'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=255, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='agreement',
            field=models.CharField(max_length=6, verbose_name='agreement'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='authority',
            field=models.CharField(max_length=10, verbose_name='authority'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='birth_day',
            field=models.DateField(verbose_name='birth day'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='root department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.District', verbose_name='district'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=45, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('2', 'male'), ('1', 'female')], default='2', max_length=1, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_badge_printed',
            field=models.BooleanField(default=False, verbose_name='is badge printed?'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_badge_returned',
            field=models.BooleanField(default=False, verbose_name='is badge returned?'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=45, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='login',
            field=models.CharField(max_length=9, verbose_name='login'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='number',
            field=models.CharField(error_messages={'unique': 'Мундай номер бар.'}, max_length=255, unique=True, validators=[django.core.validators.RegexValidator(message='must be in 123456789 format!', regex='^\\d{9}$')], verbose_name='number'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='passport_num',
            field=models.CharField(max_length=7, verbose_name='number of passport'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(max_length=13, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='patronymic',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='patronymic'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(upload_to='users/img', verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='plot',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='enumerator plot'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='qrcode',
            field=models.ImageField(blank=True, null=True, upload_to='users/qr-codes', verbose_name='QR code'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.CharField(choices=[('enum', 'Enumerator'), ('ins', 'Instructor'), ('cor', 'Coordinator')], default=('cor', 'Coordinator'), max_length=50, verbose_name='role'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sector',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='coordinator sector'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='serial',
            field=models.CharField(choices=[('ID', 'ID'), ('AN', 'AN'), ('AC', 'AC')], default='ID', max_length=2, verbose_name='serial'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='territory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Territory', verbose_name='territory'),
        ),
        migrations.AlterField(
            model_name='region',
            name='address',
            field=models.CharField(max_length=255, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(choices=[('chu', 'Чүй'), ('osh', 'Ош'), ('bat', 'Баткен'), ('jal', 'Жалал-Абад'), ('tal', 'Талас'), ('nar', 'Нарын'), ('kol', 'Ысык-Көл')], max_length=9, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='territory',
            name='code',
            field=models.CharField(max_length=14, unique=True, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='territory',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.District'),
        ),
        migrations.AlterField(
            model_name='territory',
            name='name',
            field=models.CharField(max_length=90, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.District', verbose_name='district'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='is staff'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='super user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Region', verbose_name='region'),
        ),
    ]
