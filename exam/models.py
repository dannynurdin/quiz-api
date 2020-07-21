from django.db import models

# class Laguage(models.Model):
#     name = models.CharField(max_length=64)
#     paradigm = models.CharField(max_length=64)

#     def __str__(self):
#         return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Difficult(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    difficult = models.ForeignKey(Difficult, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    corect_answer = models.CharField(max_length=50)
    incorect_answer_0 = models.CharField(max_length=50)
    incorect_answer_1 = models.CharField(max_length=50)
    incorect_answer_2 = models.CharField(max_length=50)

    def __str__(self):
        return self.name
