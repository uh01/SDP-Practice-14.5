# Generated by Django 4.2.7 on 2023-12-07 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='department',
            field=models.TextField(default='exit'),
            preserve_default=False,
        ),
    ]
