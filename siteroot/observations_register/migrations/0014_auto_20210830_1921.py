# Generated by Django 3.2.6 on 2021-08-30 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations_register', '0013_auto_20210830_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='neo_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='ref_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
