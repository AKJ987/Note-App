# Generated by Django 4.1 on 2022-08-19 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotesModel',
            fields=[
                ('title', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('note', models.CharField(max_length=19999)),
                ('image', models.ImageField(null=True, upload_to='images')),
            ],
        ),
    ]
