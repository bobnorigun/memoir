from django.db import models
from django.urls import reverse

# Genre 필요한가? 카테고리 나중에 필요할지도
class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Tool)")

    #verbose name이 없으니 폼에서 Name으로 명명될 것
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)

    #Author는 필요없음.
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    #ISBN도 필요없음. 유니크 아이디생성인데 불필요.
    #ManyToManyField used because genre can contain many books. Books can cover many genres.
    #Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Return the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

#BookInstance는 불필요.
#Author는 불필요.

# Create your models here.
class PapaAbb(models.Model):
    """Model representing a Book"""
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the app")
    coverimage = models.ImageField(upload_to='images/', blank=True, null=True)
    coverimage2 = models.ImageField(upload_to='images/', blank=True, null=True)
    releasenote = models.TextField(max_length=1000, help_text="Enter a brief description of the app")

    # Metadata
    class Meta:
        ordering = ['-title']

    #releasenote split, 소 뒷걸음치다가 쥐잡은 격._as_list가 명령어로군.
    def releasenote_as_list(self):
        return self.releasenote.split('br')

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('abb-detail', args=[str(self.id)])
