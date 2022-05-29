# Generated by Django 4.0.4 on 2022-05-24 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersData', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='commonPacksOpened',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userdata',
            name='defeat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userdata',
            name='newUser',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='rarePacksOpened',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userdata',
            name='specialPacksOpened',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userdata',
            name='win',
            field=models.IntegerField(default=0),
        ),
    ]
