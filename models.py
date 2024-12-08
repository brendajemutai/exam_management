from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="results")
    subject = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.subject}"

class Parent(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="parent")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
