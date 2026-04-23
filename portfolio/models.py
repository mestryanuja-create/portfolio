from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default='Developer')
    description = models.TextField()
    technologies = models.TextField(default='')
    clients = models.CharField(max_length=200, default='Enterprise clients globally')
    image = models.ImageField(upload_to='static/portfolio_images/', default='default_image.png', blank=True, null=True)

    def __str__(self):
        return self.title