# Generated by Django 3.2 on 2022-02-05 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('render', '0002_auto_20220205_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='status',
            field=models.CharField(default='PROCESSING', max_length=24),
        ),
    ]
