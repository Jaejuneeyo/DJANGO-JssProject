from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
# Create your views here.

def signup(request):
    regi_form = UserCreationForm() #django에서 제공해주는 UserCreationForm 사용-regi_form으로 적용
    if request.method =="POST": #POST 방식 적용
        filled_form = UserCreationForm(request.POST) #POST 방식이 요청된 UserCreationForm을 filled_form으로 적용
        if filled_form.is_valid(): #유효성 검사 통과시
            filled_form.save() #filled_form 저장
            return redirect('index') #index 페이지로 보내줌
        

    return render(request, 'signup.html',{'regi_form':regi_form})  #signup.html에 regi_formd의 정보를 담아 화면 전송

class MyLoginView(LoginView): #LoginView를 MyLoginView에 상속(오버라이딩)
    template_name = 'login.html' #템플릿 이름 변경(login.html로)