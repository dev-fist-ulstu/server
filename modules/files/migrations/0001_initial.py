# Generated by Django 5.1.3 on 2024-12-22 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(max_length=4000)),
                ('filename', models.CharField(max_length=255)),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'fs_file',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='FileType',
            fields=[
                ('file_type', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField()),
                ('save_path', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
            options={
                'db_table': 'fs_file_type',
            },
        ),
    ]
