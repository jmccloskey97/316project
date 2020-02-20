from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    url = models.CharField(max_length=100)
    score = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    best_new_music = models.BooleanField()

class Artist(models.Model):
    name = models.CharField(max_length=100)
    review = models.ForeignKey(Review, on_delete=models.PROTECT)

class Content(models.Model):
    data = models.CharField(max_length=100)
    review = models.ForeignKey(Review, on_delete=models.PROTECT)

class Genre(models.Model):
    genre = models.CharField(max_length=100)
    review = models.ForeignKey(Review, on_delete=models.PROTECT)

class Label(models.Model):
    label = models.CharField(max_length=100)
    review = models.ForeignKey(Review, on_delete=models.PROTECT)

class Author(models.Model):
    name = models.CharField(max_length=100)
    review = models.ForeignKey(Review, on_delete=models.PROTECT)


#cd myproject/myrproject
#python3 manage.py makemigrations
#python3 manage.py migrate
#python3 manage.py createsuperuser
#python3 manage.py runserver
#sqlite3 db.sqlite3 
