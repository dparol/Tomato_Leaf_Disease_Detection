from django.db import models

# Create your models here.

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='images/')
    predicted_disease = models.CharField(max_length=100, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
