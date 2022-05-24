from django.db import models

# Create your models here.

class ApiError(models.Model):
    ip_address = models.CharField(max_length=255, blank=True)
    error_type = models.CharField(max_length=255)
    error_stack_trace = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.error_type, self.ip_address, self.timestamp.strftime("%Y-%m-%d %I:%M %p"))
