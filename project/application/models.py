from django.db import models

# Create your models here.

class register(models.Model):
    Name=models.CharField(max_length=100)
    Address=models.CharField(max_length=20)
    Username=models.CharField(max_length=500)
    Password=models.CharField(max_length=20)

class Project(models.Model):
    Project_Name = models.CharField(max_length=20)
    Description = models.CharField(max_length=100,null=True)
    Assigned_Date=models.DateField()
    Deadline_Date = models.DateField()
    State = models.IntegerField(default=False)

class Task(models.Model):
    Project_Id = models.IntegerField()
    Task_Id = models.CharField(max_length=20,null=True)
    Tasks_Name = models.CharField(max_length=20)
    State = models.IntegerField(default=0)

class Ticket(models.Model):
    Ticket_Id= models.CharField(max_length=20, null=True)
    Task_Id = models.CharField(max_length=20, null=True)
    Ticket_Name = models.CharField(max_length=20)
    Status = models.CharField(max_length=100, null=True)
    Developer_Name = models.CharField(max_length=20)
    Dev_des = models.CharField(max_length=100, null=True)
    State = models.IntegerField(default=0)

