# Generated by Django 4.0.4 on 2022-06-17 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_alter_cars_options_cars_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='color',
            field=models.CharField(choices=[('black', 'black'), ('white', 'white'), ('red', 'red'), ('green', 'green')], default='black', max_length=20),
        ),
    ]
