from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


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
    parentRegion = models.ForeignKey("self", on_delete=models.CASCADE)

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
    picture = models.ImageField(upload_to='wine', null=True, blank=True)

    def __str__(self):
        return ", ".join([self.designation, self.appellation, self.winery, self.varietal, self.vineyard])


class UserLogIn(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class UserInformation(models.Model):
    phoneMessage = 'Phone number must be entered in the format: 9999999999'
    phoneRegex = RegexValidator(
        regex=r'^\d{10}$',
        message=phoneMessage
    )

    user = models.ForeignKey(UserLogIn, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    DoB = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=10, validators=[phoneRegex], blank=True, null=True)

    def __str__(self):
        return self.firstName + " " + self.lastName


class Rating(models.Model):
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)
    vintage = models.PositiveSmallIntegerField(validators=(MinValueValidator(1900), MaxValueValidator(datetime.date.today().year)))
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
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
