# Generated by Django 3.2 on 2022-11-20 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('review', models.TextField()),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
