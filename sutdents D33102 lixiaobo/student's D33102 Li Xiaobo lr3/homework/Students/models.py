from django.db import models


class discipline(models.Model):
    discipline = models.CharField(max_length=50)

class tercher(models.Model):
    name = models.CharField(max_length=50)
    id_discipline = models.ForeignKey(discipline, null=True, blank=True, on_delete=models.SET_NULL)


class homework(models.Model):
    execution_period = models.IntegerField()
    task_text = models.CharField(max_length=100)
    date_issue = models.DateTimeField()
    penalty = models.CharField(max_length=100)
    id_discipline = models.ForeignKey(discipline, null=True, blank=True, on_delete=models.SET_NULL)


class student(models.Model):
    name = models.CharField(max_length=50)


class performance(models.Model):
    score = models.IntegerField(max_length=20,null=True,blank=True)
    Completion_date = models.DateTimeField(null=True,blank=True)
    id_homeworke = models.ForeignKey(homework, null=True, blank=True, on_delete=models.SET_NULL)
    id_student = models.ForeignKey(student, null=True, blank=True, on_delete=models.SET_NULL)
