from django.db import models


class Publisher(models.Model):
    class Meta:
        db_table = 'bookstore_publishers'

    name = models.CharField(max_length=255, blank=False, unique=True)
    num_awards = models.PositiveIntegerField()

