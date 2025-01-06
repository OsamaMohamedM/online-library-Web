from django.db import models# type: ignore

from django.db import models# type: ignore

# Create your models here.

# Create your models here.
from django.db import models # type: ignore

CATEGORY_CHOICES = [
    ('function', 'Function'),
    ('Science Fiction', 'Science Fiction'),
    ('Fantasy', 'Fantasy'),
    ('Historical', 'Historical'),
    ('Horror', 'Horror'),
    ('Romance', 'Romance'),
    ('Mystery', 'Mystery'),
]

class books(models.Model):
    id = models.AutoField(primary_key=True)
    tittle = models.CharField(max_length=30,default='', null=True)
    description = models.TextField(null=True)
    num_of_pages = models.PositiveIntegerField(default=0, null=True)
    price = models.CharField(max_length=7, default='0',null=True)
    image = models.ImageField(upload_to='media/photo/' ,null=False)
    book_link = models.ImageField(upload_to='books', null=True)
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=30, null=True, choices=CATEGORY_CHOICES)
    author = models.CharField(max_length=50,null=True)
    language = models.CharField(max_length=15, null=True)
    year = models.CharField(max_length=4, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            max_id = books.objects.all().aggregate(models.Max('id'))['id__max'] or 0
            self.id = max_id + 1
        super(books, self).save(*args, **kwargs)
    def __str_(self):
         return self.tittle  
    class Meta:
        verbose_name = 'books' ;  
types = [
    ('admin','admin'),
    ('user','user')
]
class user(models.Model):
    id = models.IntegerField(primary_key=True )
    name = models.CharField(max_length=30)
    age =models.IntegerField(default=18)
    phone = models.CharField(max_length=14)
    email =models.EmailField()
    password = models.CharField(max_length=15)
    type  = models.CharField(max_length=5,choices=types) 
    borrowedBooks = models.ManyToManyField(books,null=True)
    def __str_(self):
         return self.name  
    class Meta:
        verbose_name = 'users' ; 

