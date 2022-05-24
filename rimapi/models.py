from django.db import models

# Create your models here.

class ApiError(models.Model):
    error_type = models.CharField(max_length=255)
    error_stack_trace = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
