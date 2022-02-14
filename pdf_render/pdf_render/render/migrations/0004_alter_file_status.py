# Generated by Django 3.2 on 2022-02-14 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('render', '0003_file_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='status',
            field=models.CharField(choices=[('DONE', 'Done'), ('PROCESSING', 'Processing')], default='PROCESSING', max_length=24),
        ),
    ]
