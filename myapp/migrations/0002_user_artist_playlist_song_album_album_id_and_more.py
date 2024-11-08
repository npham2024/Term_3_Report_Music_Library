# Generated by Django 4.2.16 on 2024-11-05 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'db_table': 'User',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artist_id', models.AutoField(primary_key=True, serialize=False)),
                ('artist_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Artist',
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('playlist_id', models.AutoField(primary_key=True, serialize=False)),
                ('playlist_name', models.CharField(max_length=255)),
                ('created_date', models.DateField()),
                ('user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'Playlist',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('song_title', models.CharField(max_length=255)),
                ('duration', models.DecimalField(decimal_places=2, max_digits=5)),
                ('artist_id', models.IntegerField()),
                ('album_id', models.IntegerField()),
            ],
            options={
                'db_table': 'Song',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='album_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist_id',
            field=models.IntegerField(),
        ),
        migrations.AlterModelTable(
            name='album',
            table='Album',
        ),
        migrations.CreateModel(
            name='PlaylistSong',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('playlist_id', models.IntegerField()),
                ('song_id', models.IntegerField()),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'db_table': 'Playlist_Song',
                'ordering': ['order'],
                'managed': True,
                'unique_together': {('playlist_id', 'song_id')},
            },
        ),
    ]
