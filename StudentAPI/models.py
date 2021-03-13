from django.db import models

# Create your models here.
class Address(models.Model):
    city = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    postal_address = models.CharField(max_length=250)

    def __str__(self):
        return '%s %s %s' % (self.postal_address, self.landmark, self.city)

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    standard = models.PositiveSmallIntegerField(default=0)
    address = models.ForeignKey(Address,related_name='address', on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name



