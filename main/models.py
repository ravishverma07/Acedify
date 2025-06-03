from django.db import models


SEMESTER_CHOICES = [
    ('1', 'Semester 1'),
    ('2', 'Semester 2'),
    ('3', 'Semester 3'),
    ('4', 'Semester 4'),
    ('5', 'Semester 5'),
    ('6', 'Semester 6'),
    ('7', 'Semester 7'),
    ('8', 'Semester 8'),
    ('none', 'None'), 
]

class Book(models.Model):
    """Model representing a book"""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    semester = models.CharField(max_length=4, choices=SEMESTER_CHOICES, null=True, blank=True)
    image = models.ImageField(upload_to='book_covers/', null=True, blank=True)

    def __str__(self):
        return self.title
    
class PreviousPaper(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    semester = models.CharField(max_length=4, choices=SEMESTER_CHOICES, null=True, blank=True)  
    file = models.FileField(upload_to='previous_papers/')

    def __str__(self):
        return self.title
