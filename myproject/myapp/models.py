from django.db import models

gender=(("1","Male"),
    ("2","Female"),
    ("3","Others"))

status=(("1","pending"),
    ("2","completed"))

# Create your models here.
class User_Model(models.Model):
    Phone_number=models.CharField(max_length=15, unique=True)
    Email = models.EmailField(max_length=254)
    is_customer=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=True)
    def __str__(self):
        return(self.Email)


class userProfileModel(models.Model):
	User_Model=models.OneToOneField(User_Model, 
          on_delete = models.CASCADE, primary_key = True)
	Name=models.CharField(max_length=100)
	Date_of_birth=models.DateField()
	Gender_choice=models.CharField(max_length=10,choices=gender)
	Image=models.ImageField(upload_to='bat_imgs/',default=True)
def __str__(self):
    return(self.Name)

class userloginotpModel:
	owner=models.ForeignKey(User_Model,on_delete=models.CASCADE)
	Otp=models.IntegerField()
	active=models.BooleanField(default=True)


class productMainModel(models.Model):
    Title=models.CharField(max_length=100)
    Description=models.CharField(max_length=100)
    Price=models.IntegerField()
    unique_code=models.CharField(max_length=100, unique=True) 
    def __str__(self):
        return(self.Title)

class UserCartProductModel:
	owner=models.ForeignKey(User_Model,on_delete=models.CASCADE)
	product=models.ForeignKey(productMainModel,on_delete=models.CASCADE)
	status_choice=models.CharField(max_length=10,choices=status)
    
class productImageModel(models.Model):
    Product=models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    Image=models.ImageField(upload_to='bat_imgs/',default=True)

class getproduct(models.Model):
    Product=models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    
    def __str__(self):
        return(self.Product.Title)