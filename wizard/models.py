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
    def __str__(self):
        """String for representing the Model object."""
        if self.question == None:
            return "Question: None" + " Answered: " + self.text
        else:
            return "Question: "+ self.question.question + " Answered: " + self.text


class Destination(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    name = models.CharField(
        max_length=200,
        help_text="Enter a desination name (e.g. Peniche etc)"
        )
    description = models.CharField(
        max_length=200,
        help_text="Enter a description for this destination",
        default = "No description has yet been written for this destination"
        )

    long_description = models.TextField(
        max_length=2000,
        help_text="Enter a longer description for this destination",
        default = "No long description has yet been written for this destination"
        )

    main_image = models.ImageField(upload_to='main_images', blank = False)

    iframe_map = models.URLField(
        max_length=500,
        help_text="Paste google maps embedd code here or 'None' if empty",
        default = "None"
        )


    """image=models.ImageField(upload_to='destination_image', blank = True)"""

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class BulletPoint(models.Model):
    destination = models.ForeignKey('Destination', on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=200)
    



class Image(models.Model):
	destination = models.ForeignKey('Destination', on_delete=models.SET_NULL, null=True)
	image = models.ImageField(upload_to='any_image', blank = False)
	caption = models.CharField(
        max_length=200,
        help_text="Enter a caption for the image"
        )


class Persona(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    name = models.CharField(
        max_length=200,
        help_text="Enter a name for the persona (e.g. First timer etc)"
        )
    description = models.CharField(
        max_length=200,
        help_text="Enter a description for the persona (e.g. Wants to surf for the first time etc)",
        null=True
        )
    destination = models.ManyToManyField(Destination, help_text='Select destinations where this persona would be happy to go')
    
    answer = models.ManyToManyField(Answer, help_text='Select the answers that indicates this persona')
    #persona = models.ManyToManyField(self.Persona, help_text='Select personas that would go to this destination')


    def display_destination(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(destination.name for destination in self.destination.all()[:3])
    
    display_destination.short_description = 'Destinations'

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

class Post(models.Model):
	post = models.TextField(max_length=500)



