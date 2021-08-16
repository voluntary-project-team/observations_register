# Generated by Django 3.1.5 on 2021-08-15 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations_register', '0002_auto_20210815_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='elem_area',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='elem_borders',
            field=models.CharField(choices=[('ЧЕТКИЕ', 'Четкие'), ('НЕЧЕТКИЕ', 'Нечеткие')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='elem_color',
            field=models.CharField(choices=[('КРАСНЫЙ', 'Красный'), ('БЕЖЕВЫЙ', 'Бежевый'), ('КОРИЧНЕВЫЙ', 'Коричневый'), ('ЧЕРНЫЙ', 'Черный')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='elem_size',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='elem_symmetry',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='inclusions',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='skin_tumors_in_fam',
            field=models.BooleanField(null=True),
        ),
    ]