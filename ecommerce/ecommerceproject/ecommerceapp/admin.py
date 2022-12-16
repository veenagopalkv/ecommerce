from django.contrib import admin
from .models import Category, product


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class productAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','stock','available','datecreated','datemodified']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20
admin.site.register(product, productAdmin)
