# Generated by Django 3.0.7 on 2020-07-02 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('posts', '0005_auto_20200702_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='post', to='categories.Category'),
        ),
    ]
