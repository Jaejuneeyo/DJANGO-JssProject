from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Jasoseol(models.Model): #models.Model을 상속 받아서 Jasoseol 모델 제작(첫글자 대문자)
    title = models.CharField(max_length=50) #제목에 짧은 문자열 적용(최대 50자)
    content = models.TextField() #내용에 긴 문자열 적용
    update_at = models.DateTimeField(auto_now=True) #시간,날짜 자동 업데이트
    author = models.ForeignKey(User, on_delete=models.CASCADE) #Fk로 연결로 연결된 jasoseol 객체를 지움

class Comment(models.Model): #Comment 모델 생성
    content = models.CharField(max_length=100) #내용에 문자열 적용(최대 100자)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #Fk로 연결로 연결된 객체를 지움(이용자)
    Jasoseol = models.ForeignKey(Jasoseol, on_delete=models.CASCADE) #Fk로 연결로 연결된 객체를 지움(자소설)