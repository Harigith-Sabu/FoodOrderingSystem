from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        db_table='category'
        
    def __str__(self):
        return self.name

class product(models.Model):
    name=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    img=models.ImageField(upload_to='product')
    desc=models.TextField()
    stock=models.IntegerField()
    avaiable=models.BooleanField()
    price=models.IntegerField()
    category=models.ForeignKey(category, on_delete=models.CASCADE)
    
    class Meta:
        db_table='product'

    # def get_url(self):
        # return reverse('details',args=[self.category.slug,self.slug])

    def __str__(self):
        return self.name

class cartlist(models.Model):
    cart_id=models.CharField(max_length=250,unique=True)
    date_added=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table='cartlist'

    def __str__(self):
        return self.cart_id

class item(models.Model):
    prodt=models.ForeignKey(product, on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist, on_delete=models.CASCADE)
    quan=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='item'

    def __str__(self):
        return self.prodt
    
    def total(self):
        return self.prodt.price*self.quan

