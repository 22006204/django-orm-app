# Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![ERdiagram](https://user-images.githubusercontent.com/118787261/208726731-9256447c-c767-49bd-aa5f-295e02886ca6.png)



## DESIGN STEPS

### STEP 1:
Clone the repository to theia ide. start a new app inside the project folder

### STEP 2:
Tyoe the appropriate code for your table and provide appropriate data types to the columns.
### STEP 3:
Create a report about your project in readme.md file and upload the django.orm.pp folder to your remote repository.

## PROGRAM
```
from django.db import models
from django.contrib import admin
class Employee(models.Model):
    Employee_ID = models.IntegerField(max_length=8, primary_key=True)
    Employee_Name = models.CharField(max_length=100)
    Employee_Age = models.IntegerField()
    Employee_Email =models.EmailField()
    Employee_post= models.CharField(max_length=100)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('Employee_ID', 'Employee_Name','Employee_Age','Employee_Email','Employee_post')
```

## OUTPUT
![djangoapp3](https://user-images.githubusercontent.com/118787261/208726901-7a7ae197-d3ac-4f02-84c6-82c6af36a473.png)




## RESULT
Hence we developed a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).
