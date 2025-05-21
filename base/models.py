from django.db import models

# Create your models here.

class Committee(models.Model):
    name = models.CharField(max_length=200)
    mandate = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Statement(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='statements/')
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name