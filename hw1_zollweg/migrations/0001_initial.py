# Generated by Django 2.2.6 on 2019-11-12 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('genre', models.TextField()),
                ('year', models.DateField()),
                ('multiplayer', models.BooleanField()),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
