from typing import Any
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest
from django.contrib import messages

class CustomBackend(ModelBackend):
    def authenticate(self, request: HttpRequest, username: str | None = ..., password: str | None = ..., **kwargs: Any) -> AbstractBaseUser | None:
        UserModel = get_user_model()
        
        try:
            user = UserModel.objects.get(username=username)
            # 개인정보 수집 동의가 활성화 상태인지
            if not user.fAgreeCollectPersonInfor:
                messages.error(request, "개인정보 수집 동의가 체크되어야 합니다.")
                return None
            # 비밀번호 체크
            if not user.check_password(password):
                # messages.error(request, "비밀번호가 잘못되었습니다.")
                return None
            
            return user
            
        except UserModel.DoesNotExist:
            return None
        