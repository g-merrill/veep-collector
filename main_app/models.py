from django.db import models

# Create your models here.
class Character(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  actor = models.CharField(max_length=100)

  def __str__(self):
    return f'{self.name} ({self.id})'

class Quote(models.Model):
  text = models.TextField(max_length=500)
  said_by = models.ForeignKey(Character, related_name='said_by',on_delete=models.CASCADE)
  aimed_at = models.ForeignKey(Character, null=True, blank=True, related_name='aimed_at', on_delete=models.CASCADE)

  def __str__(self):
    return f'Quote {self.id}'