from django.contrib import admin
from catalog.models import Product, Category


# admin.site.register(Product)
# admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ['category']
    list_display = ('id', 'name', 'category', 'price')
    search_fields = ('name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category')
