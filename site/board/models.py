from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200) #질문 제목
    content = models.TextField() #질문 내용
    file = models.FileField(upload_to='uploads/', blank=True, null=True) #파일 업로드(이미지/동영상 포함)
    author = models.CharField(max_length=100) #질문 작성자 이름
    created_at = models.DateTimeField(auto_now_add=True) #생성 시간
    updated_at = models.DateTimeField(auto_now=True) #수정 시간
    is_resolved = models.BooleanField(default=False) # 해결 여부

    def __str__(self):
        return self.title

    