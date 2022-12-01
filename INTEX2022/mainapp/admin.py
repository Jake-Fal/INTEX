from django.contrib import admin
from .models import UserInfo, WaterEntry,FoodEntry,FoodItem,Login,MealClass,Actuals,Goal

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(WaterEntry)
admin.site.register(FoodEntry)
admin.site.register(FoodItem)
admin.site.register(Login)
admin.site.register(MealClass)

admin.site.register(Actuals)
admin.site.register(Goal)

