from django.db import models

# Create your models here.
class Dept(models.Model):
    deptNo=models.IntegerField(primary_key=True)
    dName=models.CharField(max_length=100,unique=True)
    loc=models.CharField(max_length=100)
    def __str__(self):
        return str(self.deptNo)
   
    

class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.DecimalField(decimal_places=2,max_digits=10)
    comm=models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=10)
    hireDate=models.DateField(auto_now_add=True)
    deptNo=models.ForeignKey(Dept,on_delete=models.CASCADE)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return str(self.empno)


class SalGrade(models.Model):
    grade=models.IntegerField(primary_key=True)
    losal=models.DecimalField(decimal_places=2,max_digits=10)
    hisal=models.DecimalField(decimal_places=2,max_digits=10)
    
