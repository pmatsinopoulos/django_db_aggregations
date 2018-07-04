from django.db import models


class Author(models.Model):
    class Meta:
        db_table = 'bookstore_authors'

    name = models.CharField(max_length=255, blank=False, unique=True)
    age = models.PositiveSmallIntegerField(blank=False)

