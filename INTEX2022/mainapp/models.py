from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Unit(models.Model):
    UnitName = models.CharField(max_length=20, null=False)
 
    class Meta:
        db_table = 'meal_units'
 
    def __str__(self):
        return self.UnitName

class MealClass(models.Model):
    MealName = models.CharField(max_length=10, null=False)
 
    class Meta:
        db_table = 'meal_class'
 
    def __str__(self):
        return self.MealName

class User(models.Model):
    FirstName = models.CharField(max_length=50, null=False)
    LastName = models.CharField(max_length=50, null=False)
    DOB = models.DateField()
    HeightFt = models.SmallIntegerField()
    HeightIn = models.SmallIntegerField()
    Weight = models.SmallIntegerField()
    Sex = models.CharField(max_length=20, null=False)

 
    class Meta:
        db_table = 'user'
 
    def __str__(self):
        return f'{self.FirstName} {self.LastName}'
class Login(models.Model):
    userID = models.ForeignKey(User, on_delete= models.CASCADE)
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=20, null=False)
 
    class Meta:
        db_table = 'login'
 
    def __str__(self):
        return self.username

class FoodItem(models.Model):
    FoodName = models.CharField(max_length=300, null=False)
    Sodium_mg = models.SmallIntegerField(max_length=20, null=True)
    Potassium_mg = models.SmallIntegerField(max_length=20, null=True)
    Phosphate_mg = models.SmallIntegerField(max_length=20, null=True)
    Protein_g = models.SmallIntegerField(max_length=20, null=True)
    Water_L = models.SmallIntegerField(max_length=20, null=True)

 
    class Meta:
        db_table = 'food_item'
 
    def __str__(self):
        return self.FoodName

class FoodEntry(models.Model):
    UserID = models.ForeignKey(User,on_delete= models.DO_NOTHING)
    MealName = models.ForeignKey(MealClass,on_delete= models.DO_NOTHING)
    FoodID = models.ForeignKey(FoodItem,on_delete= models.DO_NOTHING)
    DateTime = models.DateTimeField(null=False)
    NumServings = models.DecimalField(max_digits=4,decimal_places=2,null=False)

 
    class Meta:
        db_table = 'food_entry'
 
    def __str__(self):
        return self.DateTime

class WaterEntry(models.Model):
    UserID = models.ForeignKey(User,on_delete= models.DO_NOTHING)
    DateTime = models.DateTimeField(null=False)
    Amount = models.DecimalField(max_digits=4,decimal_places=2,null=False)

 
    class Meta:
        db_table = 'water_entry'
 
    def __str__(self):
        return self.DateTime