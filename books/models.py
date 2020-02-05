from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    photo = models.FileField()

    def __str__(self):
        return self.firstName


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    file_type = models.CharField(max_length=10)
    cover_photo = models.FileField()
    book_file = models.FileField()
    ownwer = models.ForeignKey(User, related_name="books",
                               on_delete=models.CASCADE, null=True)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.title
