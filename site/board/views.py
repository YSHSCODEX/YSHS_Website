

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .forms import QuestionForm

#질문 목록 보기
def question_list(request):
    questions = Question.objects.all().order_by('-created_at') #최신 질문 순 정렬
    return render(request, 'questions/question_list.html', {'questions': questions})

#질문 상세 보기
def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'questions/question_detail.html', {'question': question})

#질문 작성 뷰
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid(): #유효한 폼이 제출되면 저장
            form.save()
            return redirect('question_list') #질문 목록 페이지로 돌아감
        
    else:
        form = QuestionForm() #빈 폼을 보여줌
    return render(request, 'questions/create_question.html', {'form': form})
        
