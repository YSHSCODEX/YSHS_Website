from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_resolved') #관리자 페이지에서 표시할 필드
    list_filter = ('is_resolved', 'created_at') #필터 추가
    search_fields = ('title', 'author') #검색 가능 필드