from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserForm(UserCreationForm):
    '''
    grade = forms.ChoiceField(choices=[(i, f'{i}st grade') for i in range(1, 4)], label='학년')
    classNum = forms.ChoiceField(choices=[(i, f'class {i}') for i in range(1, 10)], label='반')
    studentNum = forms.ChoiceField(choices=[(i, f'number {i}') for i in range(1, 40)], label='출석번호')
    birthDate = forms.DateField(label='생년월일', widget=forms.SelectDateWidget(years=range(1900, 2100)))
    email = forms.EmailField(label='개인 이메일 주소', required=False)
    # username 아이디
    # password1 비밀번호1
    # password2 비밀번호 확인
    '''
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('grade', 'classNum', 'studentNum', 'birthDate', 'email', 'fAgreeCollectPersonInfor')