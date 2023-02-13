from django.contrib import admin

from . import models
# Register your models here.
admin.site.register(models.User_Model)

admin.site.register(models.userProfileModel)
# admin.site.register(models.userloginotpModel)
admin.site.register(models.productMainModel)
# admin.site.register(models.UserCartProductModel)
admin.site.register(models.productImageModel)
admin.site.register(models.getproduct)