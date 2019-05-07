from django.db import models

# Create your models here.
class Question(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    question = models.CharField(max_length=200)
    priority = models.CharField(max_length=200)
    
    
    def __str__(self):
        """String for representing the Model object."""
        return self.question
    
    
class Answer(models.Model):
	question = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True)
	text = models.CharField(max_length=200)



class Destination(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    name = models.CharField(
        max_length=200,
        help_text="Enter a desination name (e.g. Peniche etc)"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name
