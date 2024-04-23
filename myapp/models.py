from django.db import models

# Create your models here.
class Departments(models.Model):
    department_name=models.CharField(max_length=100)
    department_details=models.TextField()
    def __str__(self):
        return self.department_name

class Doctors(models.Model):
    doctor_name=models.CharField(max_length=100)
    doctor_special=models.CharField(max_length=100)
    department_name=models.ForeignKey(Departments,on_delete=models.CASCADE)
    doctor_img=models.ImageField(upload_to='doctors')
    def __str__(self):
        return self.doctor_name

class Booking(models.Model):
    Patient_Name=models.CharField(max_length=100)
    Mobile_No=models.CharField(max_length=100)
    Email_Id=models.EmailField()
    doctor_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    Booking_Date=models.DateField()
    Booking_Time=models.TimeField()
    Booking_On=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Patient_Name


