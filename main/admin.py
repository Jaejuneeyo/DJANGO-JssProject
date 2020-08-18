from django.contrib import admin
from .models import Jasoseol, Comment #Jasoseol, Comment 모델 등록
# Register your models here.

admin.site.register(Jasoseol) #Jasoseol 파일 등록

admin.site.register(Comment) #comment 파일 등록