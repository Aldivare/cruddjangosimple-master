# Generated by Django 4.0.6 on 2022-07-17 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplecrud', '0007_remove_crudsimple_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crudsimple',
            name='gender',
            field=models.CharField(choices=[('Pria', 'Pria'), ('Wanita', 'Wanita')], max_length=50),
        ),
    ]
