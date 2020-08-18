from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Jasoseol(models.Model): #models.Model을 상속 받아서 Jasoseol 모델 제작(첫글자 대문자)
    title = models.CharField(max_length=50) #제목에 짧은 문자열(50자 제한 필수)
    content = models.TextField() #내용에 긴 문자열 입력 가능
    undated_at = models.DateTimeField(auto_now=True) #날짜와 시간을 받을 수 있게함(자동 업데이트 저장)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #FK로 연결로 객체를 지움

class Comment(models.Model): #models.Model을 상속 받아 Comment 모델 제작(첫글자 대문자)
    content = models.CharField(max_length=100) #내용에 짧은 문자열 100자 이내
    author = models.ForeignKey(User, on_delete=models.CASCADE) #FK로 연결로 객체를 지움(이용자)
    jasoseol = models.ForeignKey(Jasoseol, on_delete=models.CASCADE) #FK로 연결로 객체를 지움(자소서)