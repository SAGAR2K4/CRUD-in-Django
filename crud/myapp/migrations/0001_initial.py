# Generated by Django 5.0 on 2023-12-21 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('semester', models.IntegerField()),
                ('division', models.CharField(max_length=3)),
            ],
        ),
    ]
