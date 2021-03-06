# Generated by Django 3.1.5 on 2021-08-29 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations_register', '0009_auto_20210824_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='eyes_col',
            field=models.CharField(choices=[('Голубой', 'Голубой'), ('Серый', 'Серый'), ('ЗЕЛЕНЫЙ', 'Зеленый'), ('КАРИЙ', 'Карий')], max_length=7),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='elem_symmetry',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='inclusions',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
