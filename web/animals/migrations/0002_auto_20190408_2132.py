# Generated by Django 2.0.13 on 2019-04-08 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='type',
            new_name='animaltype',
        ),
        migrations.AddField(
            model_name='animal',
            name='animalid',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
