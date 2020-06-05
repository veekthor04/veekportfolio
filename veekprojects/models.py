from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/%Y/%m/%d', blank=True)
    last_updated = models.DateField(auto_now=True)
    project_link = models.CharField(max_length=200)
    project_status = models.CharField(max_length=9, choices=(("pending","pending"),("completed","completed"),("aborted","aborted")), default="completed")

    def __str__(self):
        return self.title
