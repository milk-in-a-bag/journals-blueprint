import os
from django.db import models

def clean_filename(filename):
    """Cleans up filename by removing extension, replacing underscores/dashes with spaces, and capitalizing."""
    name = os.path.splitext(filename)[0]
    name = name.replace('_', ' ').replace('-', ' ').title()
    return name

class Committee(models.Model):
    name = models.CharField(max_length=200)
    mandate = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Statement(models.Model):
    name = models.CharField(max_length=200, blank=True)
    file = models.FileField(upload_to='statements/')
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, related_name='statements')
    uploaded_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.file:
            try:
                # Gets the original uploaded filename (not the saved name with suffixes)
                original_filename = self.file.file.name
            except AttributeError:
                original_filename = self.file.name
            self.name = clean_filename(os.path.basename(original_filename))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
