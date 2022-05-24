from django.db import models

# Create your models here.


class Question:
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name
