from django.db import models

class Question(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    question=models.TextField()

    def __str__(self):
        return self.question

class Answer(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    answer=models.TextField()
    question=models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.name