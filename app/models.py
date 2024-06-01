import random

from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from random import randint
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

from django.db.models import Avg


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)
    abbreviation = models.CharField(blank=True, max_length=4)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    parentRegion = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Appellation(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey("Region", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Winery(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Varietal(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Wine(models.Model):
    WINE_TYPES = (
        ('White', 'White'),
        ('Red', 'Red'),
        ('Rosé', 'Rosé'),
        ('Sparkling', 'Sparkling'),
        ('Dessert', 'Dessert'),
        ('Fortified', 'Fortified'),
        ('Other', 'Other')
    )
    designation = models.CharField(max_length=50, null=True, blank=True)
    wineType = models.CharField(max_length=10, choices=WINE_TYPES)
    varietal = models.ForeignKey(Varietal, on_delete=models.CASCADE)
    winery = models.ForeignKey(Winery, on_delete=models.CASCADE)
    vineyard = models.CharField(max_length=50, blank=True)
    appellation = models.ForeignKey(Appellation, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='uploads/wine/', null=True, blank=True)

    def __str__(self):
        return ", ".join(filter(None, [self.designation, self.appellation.name, self.winery.name,
                                       self.vineyard]))

    def num_ratings(self):
        # doneTODO: return the number of reviews for each wine
        #  - 0 if there's no rating
        return Rating.objects.filter(wine=self.id).count()

    def average_rating(self):
        # DoneTODO: return the average rating of each wine - 0 if there's no
        # rating
        if Rating.objects.filter(wine=self.id).count() == 0:
            return 0
        else:
            return (Rating.objects.filter(wine=self.id)
                    .aggregate(avgRating=Avg('rating')))['avgRating']

    def average_price(self):
        # doneTODO: return the average price of each wine
        if Rating.objects.filter(wine=self.id).count() == 0:
            return 0
        else:
            return (Rating.objects.filter(wine=self.id)
                    .aggregate(avgPrice=Avg('price')))['avgPrice']


class Rating(models.Model):
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)
    vintage = models.PositiveSmallIntegerField(
        validators=(MinValueValidator(1900), MaxValueValidator(datetime.date.today().year)))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(validators=(MinValueValidator(1), MaxValueValidator(10)))
    tannin = models.PositiveSmallIntegerField(validators=(MinValueValidator(1), MaxValueValidator(3)))
    sweetness = models.PositiveSmallIntegerField(validators=(MinValueValidator(1), MaxValueValidator(5)))
    alcohol = models.PositiveSmallIntegerField(validators=(MinValueValidator(1), MaxValueValidator(3)))
    acidity = models.PositiveSmallIntegerField(validators=(MinValueValidator(1), MaxValueValidator(3)))
    body = models.PositiveSmallIntegerField(validators=(MinValueValidator(1), MaxValueValidator(3)))
    finish = models.PositiveSmallIntegerField(validators=(MinValueValidator(1), MaxValueValidator(3)))
    price = models.FloatField(validators=(MinValueValidator(0.0),))
    comment = models.TextField(max_length=500, null=True, blank=True)

    def sweetness_words(self):
        match self.sweetness:
            case 1:
                return "Dry"
            case 2:
                return "Off-Dry"
            case 3:
                return "Medium-Dry"
            case 4:
                return "Medium-Sweet"
            case 5:
                return "Sweet"
            case _:
                return ""

    def sweetness_bar(self):
        return self.sweetness/5 * 100

    def alcohol_words(self):
        match self.alcohol:
            case 1:
                return "Low"
            case 2:
                return "Medium"
            case 3:
                return "High"
            case _:
                return ""

    def alcohol_bar(self):
        return self.alcohol/3 * 100

    def tannin_words(self):
        match self.tannin:
            case 1:
                return "Low"
            case 2:
                return "Medium"
            case 3:
                return "High"
            case _:
                return ""

    def tannin_bar(self):
        return self.tannin/3 * 100

    def acidity_words(self):
        match self.acidity:
            case 1:
                return "Low"
            case 2:
                return "Medium"
            case 3:
                return "High"
            case _:
                return ""

    def acidity_bar(self):
        return self.acidity/3 * 100

    def body_words(self):
        match self.body:
            case 1:
                return "Light"
            case 2:
                return "Medium"
            case 3:
                return "Full"
            case _:
                return ""

    def body_bar(self):
        return self.body/3 * 100

    def finish_words(self):
        match self.finish:
            case 1:
                return "Short"
            case 2:
                return "Medium"
            case 3:
                return "Long"
            case _:
                return ""

    def finish_bar(self):
        return self.finish/3 * 100

