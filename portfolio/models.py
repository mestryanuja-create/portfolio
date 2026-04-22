from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    collaborators = models.TextField()
    technologies = models.TextField(default='Your default technologies here')
    feedback = models.TextField(default='Your default feedback here')
    image = models.ImageField(upload_to='static/portfolio_images/', default='default_image.png')

    def __str__(self):
        return self.title