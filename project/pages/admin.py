from django.contrib import admin # type: ignore
from .models import user,books

# Register your models here.
admin.site.register(user)
admin.site.register(books)
