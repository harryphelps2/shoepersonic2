from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

SHOE_TYPE_CHOICES = [
    ('flats', 'FLATS'),
    ('track spikes', 'TRACK_SPIKES'),
    ('cross country spikes', 'CROSS_COUNTRY_SPIKES'),
    ('pluggers', 'PLUGGERS')
]

GENDER_CHOICES = [
    ('Male','MALE'),
    ('Female','FEMALE')
]

class Shoe(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null=True, blank=True) 
    strapline = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    shoe_type = models.CharField(max_length=50, choices=SHOE_TYPE_CHOICES)
    weight = models.IntegerField(null=True, blank=True)
    weight_ranking = models.IntegerField(null=True, blank=True) 
    wet_weight = models.IntegerField(null=True, blank=True)
    wet_weight_ranking = models.IntegerField(null=True, blank=True)
    flexibility_ranking = models.IntegerField(null=True, blank=True)
    fit_descriptor = models.CharField(max_length=50, null=True, blank=True)
    support_ranking = models.IntegerField(null=True, blank=True) 
    spikes_included = models.CharField(null=True, max_length=100, blank=True)
    midsole_drop_height = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    primary_image = models.ImageField(null=True, blank=True)
    blog_link = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Stock(models.Model):
    shoe_model = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    size = models.DecimalField(max_digits=5, decimal_places=1)
    stock = models.IntegerField() 

    def __str__(self):
        stockline = "{0} - {1}: {2} left".format(self.shoe_model.name, self.size, self.stock)
        return stockline


class ProductImage(models.Model):
   shoe_model = models.ForeignKey(Shoe, on_delete=models.SET_NULL, null=True)
   image_url = models.ImageField(null=True, blank=True) 

   def __str__(self):
       return self.image_url
   
class CustomerReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    date = models.DateField()
    shoe_model = models.ForeignKey(Shoe, on_delete=models.SET_NULL, null=True)
    customer_overall_rating = models.IntegerField(null=True, blank=True) 
    customer_fit_rating = models.IntegerField(null=True, blank=True)
    customer_support_rating = models.IntegerField(null=True, blank=True) 
    customer_race_experience = models.TextField(null=True, blank=True)
    customer_review = models.TextField(null=True, blank=True)

    def __str__(self):
        review_line = "{0} reviewed {1} on {2}".format(self.user, self.shoe_model, self.date)
        return review_line