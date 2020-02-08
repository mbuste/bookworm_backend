from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from djongo.storage import GridFSStorage
grid_fs_storage = GridFSStorage(
    collection='media', base_url=''.join([settings.MEDIA_URL]))


class Author(models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    # photo = models.ImageField(upload_to='', storage=grid_fs_storage)
    photo = models.ImageField(upload_to='')

    def __str__(self):
        return self.firstName


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    file_type = models.CharField(max_length=10)
    # cover_photo = models.ImageField(upload_to='', storage=grid_fs_storage)
    cover_photo = models.ImageField(upload_to='', )
    book_file = models.FileField(upload_to='books', storage=grid_fs_storage)
    ownwer = models.ForeignKey(User, related_name="books",
                               on_delete=models.CASCADE, null=True)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.title
