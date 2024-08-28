from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    grade = models.IntegerField(verbose_name='학년',
                                choices=[(i, f'{i}st grade') for i in range(1, 4)],)
    classNum = models.IntegerField(verbose_name='반',
                                   choices=[(i, f'class {i}') for i in range(1, 10)],)
    studentNum = models.IntegerField(verbose_name='출석번호',
                                     choices=[(i, f'number {i}') for i in range(1, 40)],)
    # last_name 사용자 성 : 실명을 뜻함
    # first_name 사용자 이름 - 이미 있음(성은 따로)-실명을 뜻함
    birthDate = models.DateField(verbose_name='생년월일',)
    email = models.EmailField(verbose_name='개인 이메일 주소',
                              unique=True,
                              max_length=254, blank=True, null=True,)
    # username 아이디
    # password1 비밀번호1
    # password2 비밀번호 확인

    # chat gpt가 필요하데요
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True
    )
    
    

