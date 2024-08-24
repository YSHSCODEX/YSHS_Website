from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    gradeChoices = [
        (1, '1st grade')
        (2, '2nd grade')
        (3, '3rd grade')
    ]
    classNumChoices = [
        (1, 'class 1')
        (2, 'class 2')
        (3, 'class 3')
        (4, 'class 4')
        (5, 'class 5')
        (6, 'class 6')
        (7, 'class 7')
        (8, 'class 8')
        (9, 'class 9')
    ]

    grade = models.IntegerField(choices=[(i, f'{i}st grade') for i in range(1, 4)])
    classNum = models.CharField(max_length=1, choices=classNumChoices)
    studentNum = models.CharField

