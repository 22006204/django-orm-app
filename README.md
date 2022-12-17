# Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

## DESIGN STEPS

### STEP 1:

### STEP 2:

### STEP 3:



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

Include the screenshot of your admin page.


## RESULT
