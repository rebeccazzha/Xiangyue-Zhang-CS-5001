from django.db import models


class Base(models.Model):
    """
    Base Alcohol
    Used as foreign key for the full database
    Implemented for filtering
    """
    title = models.CharField(verbose_name="Base", max_length=16)


Base.objects.create(title="Vodka")
Base.objects.create(title="Whiskey")
Base.objects.create(title="Rum")
Base.objects.create(title="Tequila")
Base.objects.create(title="Gin")
Base.objects.create(title="Mixed")


class Thumbnail(models.Model):
    """
    The full database of cocktail information
    Use base alcohol as foreign key
    """
    image_url = models.CharField(max_length=255)
    label = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    base = models.ForeignKey(to="Base", to_field="id", on_delete=models.CASCADE)
