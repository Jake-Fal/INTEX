from django.contrib import admin
from .models import User, WaterEntry,FoodEntry,FoodItem,Login,MealClass,Unit
# Register your models here.
admin.site.register(User)
admin.site.register(WaterEntry)
admin.site.register(FoodEntry)
admin.site.register(FoodItem)
admin.site.register(Login)
admin.site.register(MealClass)
admin.site.register(Unit)

