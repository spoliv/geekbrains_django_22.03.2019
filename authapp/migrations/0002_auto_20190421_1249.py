# Generated by Django 2.1.7 on 2019-04-21 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(null=True, verbose_name='возраст'),
        ),
    ]
