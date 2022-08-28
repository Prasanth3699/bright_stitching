from statistics import mode
from xml.dom.minidom import Attr
from django.db import models

# Create your models here.

class safetyWears(models.Model):
    name = models.CharField(max_length=50)
    material_name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="safetyWears")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '1. Safety Wears'

    

# T-SHIRTS
class tshirts(models.Model):
    name = models.CharField(max_length=50,)
    material_name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="T-shirts")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '2. T-shirts'

# UNIFORMS
class uniforms(models.Model):
    name = models.CharField(max_length=50)
    material_name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="Uniforms")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '3. Uniforms'
    
# CAPS
class caps(models.Model):
    name = models.CharField(max_length=50)
    material_name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="Caps")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '4. Caps'
    
# CONTACT FORM DETAILS
class contactForm(models.Model):
    name = models.CharField(max_length=50)
    email= models.EmailField(unique=True)
    phone_number = models.PositiveIntegerField(unique=True)
    address = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    text = models.TextField()

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = '5. Cotact forms'