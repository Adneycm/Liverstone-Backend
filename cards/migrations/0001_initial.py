# Generated by Django 4.0.4 on 2022-05-19 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default=' ', null=True)),
                ('image', models.BinaryField()),
                ('attack', models.IntegerField(default=0, null=True)),
                ('health', models.IntegerField(default=0, null=True)),
                ('rarity', models.CharField(max_length=200)),
            ],
        ),
    ]
