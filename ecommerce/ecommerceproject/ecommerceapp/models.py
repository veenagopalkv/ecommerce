from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255,unique=True)
    slug =models.SlugField(max_length=255,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('ecommerceapp:products_by_category',args=[self.slug])

class product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='product',blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    datecreated=models.DateTimeField(auto_now_add=True)
    datemodified=models.DateTimeField(auto_now=True)


    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('ecommerceapp:categoryproductdetail',args=[self.category.slug,self.slug])