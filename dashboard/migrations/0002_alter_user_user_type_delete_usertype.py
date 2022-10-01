# Generated by Django 4.1.1 on 2022-09-06 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveIntegerField(choices=[(1, 'Student'), (2, 'Teacher')], default=1),
        ),
        migrations.DeleteModel(
            name='UserType',
        ),
    ]
