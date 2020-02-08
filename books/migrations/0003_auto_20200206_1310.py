# Generated by Django 2.2.10 on 2020-02-06 10:10

from django.db import migrations, models
import djongo.storage


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20200206_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.FileField(storage=djongo.storage.GridFSStorage(base_url='/media/media/', collection='media'), upload_to='authors'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_file',
            field=models.FileField(storage=djongo.storage.GridFSStorage(base_url='/media/media/', collection='media'), upload_to='books'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_photo',
            field=models.FileField(storage=djongo.storage.GridFSStorage(base_url='/media/media/', collection='media'), upload_to='books'),
        ),
    ]