from django.db import models
from django.urls import reverse


SEX = [
    ('m', 'male'),
    ('f', 'female')
]

class Users(models.Model):
    name = models.CharField(max_length=100,verbose_name='имя')
    surname = models.CharField(max_length=100,verbose_name='фамилия')
    age = models.IntegerField(verbose_name='возраст')
    sex = models.CharField(max_length=1, choices=SEX,verbose_name='пол')
    email = models.EmailField(null=True,verbose_name='почта')
    city = models.CharField(max_length=100, default='Minsk',verbose_name='город')

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myshop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)

    name = models.CharField(max_length=150, db_index=True)
    slug = models.CharField(max_length=150, db_index=True, unique=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    description = models.TextField(max_length=1000, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    uploaded = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'), )

    def __str__(self):
        return  self.name

    def get_absolute_url(self):
        return reverse('myshop:product_detail', args=[self.id, self.slug])