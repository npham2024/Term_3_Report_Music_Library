# Generated by Django 4.2.16 on 2024-11-05 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_playlistsong_options_remove_playlistsong_order_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='playlist',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='playlistsong',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='song',
            options={'managed': False},
        ),
    ]
