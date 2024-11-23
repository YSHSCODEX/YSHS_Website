from django.urls import path 
from . import views #뷰를 url에 연결

urlpatterns = [
    path('', views.question_list, name = 'question_list'), #질문 목록
    path('<int:question_id>/', views.question_deatil, name='question_detail'), #질문 상세
]