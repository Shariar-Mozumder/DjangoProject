from django.contrib import admin
from .models import Variant,Product,ProductImage,ProductVariant,ProductVariantPrice

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    
    
class ProductVariantPriceAdmin(admin.ModelAdmin):
    list_display = ('product_variant_one', 'price','stock')
    

# Register your models here.
admin.site.register(Variant)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductVariant)
admin.site.register(ProductVariantPrice,ProductVariantPriceAdmin)



    
