from django.contrib import admin
from app.models import *
# Register your models here.


admin.site.register(Category)
admin.site.register(Group)
admin.site.register(Colors)
admin.site.register(Size)
admin.site.register(Status)
admin.site.register(Order)


class adminTovar(admin.ModelAdmin):
    list_display = ('group','name','colors','price','discount','category')

admin.site.register(Tovar,adminTovar)

class adminOrder(admin.ModelAdmin):
    list_display = ('data','user')


class adminCart(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(Cart,adminCart)