# Generated by Django 3.2.8 on 2021-10-30 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_post_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified',
            field=models.DateField(auto_now=True),
        ),
    ]