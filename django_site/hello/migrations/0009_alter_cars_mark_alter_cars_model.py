# Generated by Django 4.0.4 on 2022-07-01 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0008_carmark_carmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='mark',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hello.carmark', verbose_name='mark'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hello.carmodel', verbose_name='model'),
        ),
    ]
