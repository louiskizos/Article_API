from django.db import models

# Create your models here.



class Article(models.Model):
    titre = models.CharField(max_length=150)
    resumer = models.CharField(max_length=255)
    date = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    image = models.ImageField(upload_to='assets/', blank=True, null=True)
    auteur = models.CharField(max_length=150)
    def __str__(self):
        return self.titre



class New(models.Model):
    email = models.CharField(max_length=255)
    def __str__(self):
        return self.titre
