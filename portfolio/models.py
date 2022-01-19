from django.db import models


class Project(models.Model):
    """Proyect model."""

    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to="portfolio/images")
    url = models.URLField(blank=True)
