from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
