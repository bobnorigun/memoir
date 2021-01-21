from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    """Model representing a Book"""
    title = models.CharField(max_length=200)
    summany = models.TextField(max_length=1000, help_text="Enter a brief description of the app")
    coverimage = models.ImageField(upload_to='images/', blank=True, null=True)
    coverimage2 = models.ImageField(upload_to='images/', blank=True, null=True)
    releasenote = models.TextField(max_length=1000, help_text="Enter a brief description of the app")

    # Metadata
    class Meta:
        ordering = ['-title']

    # Mdthods
    def get_absolute_url(self):
        """Return the url to access a detail record"""
        return reverse('app-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.title
