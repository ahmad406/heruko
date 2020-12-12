from django.db import models

# Create your models here.
class feedback(models.Model):
    mail = models.EmailField()
    feedback = models.TextField(max_length=100)
    def __str__(self):
      return str(self.email)


