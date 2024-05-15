from django.core.validators import RegexValidator
from django.db import models
import uuid
import os


class Category(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)


class Dish(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('dishes/', new_filename)

    slug = models.SlugField(max_length=200, db_index=True)
    name = models.CharField(unique=True, max_length=50, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=500, blank=True)
    ingredients = models.CharField(max_length=200)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField()
    special = models.BooleanField(default=False)
    image = models.ImageField(upload_to=get_file_name)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.price}$'

    class Meta:
        ordering = ('position', 'price')
        index_together = (('id', 'slug'),)
#
#
class Event(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('events/', new_filename)

    name = models.CharField(max_length=50, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=200, blank=True)
    paragraph_1 = models.CharField(max_length=100, blank=True)
    paragraph_2 = models.CharField(max_length=100, blank=True)
    paragraph_3 = models.CharField(max_length=100, blank=True)
    is_visible = models.BooleanField(default=True)
    image = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.name}, {self.price}$'


class Gallery(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('gallery/', new_filename)

    image = models.ImageField(upload_to=get_file_name)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)


class UserReservation(models.Model):

    mobile_re = RegexValidator(regex=r"^(\d{3}[- .]?){2}\d{4}$", message='Incorrect phone number (xxx xxx xxxx)')
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, validators=[mobile_re])
    people = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date', '-is_processed')

    def __str__(self):
        return f'{self.name}, {self.phone_number}, {self.message[:50]}'

