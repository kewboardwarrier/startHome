# Generated by Django 4.0.3 on 2022-05-15 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='업데이트',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='작성일',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
