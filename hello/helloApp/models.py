from django.db import models

# Create your models here.

class course(models.Model):
    courseCode=models.CharField(max_length=10)
    courseTitle=models.CharField(max_length=30)
    courseCredits=models.IntegerField()
    def __str__(self):
        return self.courseCode+" "+self.courseTitle+" "+str(self.courseCredits)

class student(models.Model):
    usn=models.CharField(max_length=10)
    name=models.CharField(max_length=20)
    sem=models.IntegerField()
    courses=models.ManyToManyField(course,related_name="student_set")
    def __str__(self):
        return self.usn+"("+self.name+")"
    
class project(models.Model):   
    student=models.ForeignKey(student,on_delete=models.CASCADE)
    ptitle=models.CharField(max_length=30)
    plang=models.CharField(max_length=30)
    pduration=models.IntegerField()
    
