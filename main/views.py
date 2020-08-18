from django.shortcuts import render, redirect, get_object_or_404
from .forms import JssForm, CommentForm
from .models import Jasoseol, Comment
from django.http import Http404 
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required #위 6번 줄까지 사용 함수 import
# Create your views here.

def index(request): #index 정의 
    all_jss= Jasoseol.objects.all() #Jasoseol의 객체 모두=all_jss로 대입
    return render(request,'index.html',{'all_jss':all_jss}) #index.html에 all_jss의 정보를 담아 화면 전송

def my_index(request): #my_index 함수 정의 
    my_jss = Jasoseol.objects.filter(author=request.user) #자신이 작성한 객체만 가져와 my_jss에 적용
    return render(request, 'index.html', {'all_jss': my_jss}) #index.html에 my_jss의 정보를 담아 화면 전송


@login_required(login_url='/login/') #login_required 적용 
def create(request): #create 함수 정의
    if not request.user.is_authenticated: #만약 request 유저가 인증이 안 되어있다면
        return redirect('login') #login 페이지로 보냄 

    if request.method == "POST":  #POST 방식 적용
        filled_form = JssForm(request.POST) #POST 방식이 적용된 JssForm을 filled_form에 넣어줌
        if filled_form.is_valid(): #유효성 검사 통과시
            temp_form = filled_form.save(commit=False) #잠시 저장 지연
            temp_form.author = request.user #작성자와 이용자가 같다면
            filled_form.save() #filled_form 저장
            return redirect('index') #index 페이지로 보냄
    jss_form =JssForm() #JssForm을 jss_form에 적용
    return render(request,'create.html',{'jss_form':jss_form}) #create.html에 jss_form의 정보를 담아 화면 전송

@login_required(login_url='/login/') #login_required 적용
def detail(request, jss_id): #jss_id 적용된 detail 함수 정의
    # try:
    #     my_jss = Jasoseol.objects.get(pk=jss_id)
    # except:
    #     raise Http404

    my_jss = get_object_or_404(Jasoseol, pk=jss_id) #pk 값이 없다면 404페이지를 띄움
    comment_form = CommentForm() #comment_form과 CommentForm 대응

    return render(request,'detail.html', {'my_jss':my_jss, 'comment_form':comment_form}) #detail.html에 my_jss와 comment_form의 정보를 담아 화면에 전송

def delete(request, jss_id): #request와 jss_id을 받은 delete 함수 정의
    my_jss = Jasoseol.objects.get(pk=jss_id) #objects을 가져와 my_jss에 저장
    if request.user == my_jss.author: #만약 이용자와 my_jss의 작성자가 같다면
        my_jss.delete() #my_jss를 지울 수 있음
        return redirect('index') #index 페이지로 보냄

    raise PermissionDenied #아니라면 권한 위반 메세지 출력
    

def update(request, jss_id): #jss_id의 정보를 담은 update 함수 정의
    my_jss = Jasoseol.objects.get(pk=jss_id) #특정 object my_jss에 입력
    jss_form = JssForm(instance=my_jss)  #instance에 my_jss를 넣고 이것을 jss_form이라 칭함
    if request.method == "POST": #POST 방식으로 온 request
        updated_form = JssForm(request.POST, instance=my_jss) #특정 instance를 updated_form에 POST 방식으로 지정
        if updated_form.is_valid(): #유효성 검사
            updated_form.save() #유효성 검사 통과 후 저장 
            return redirect('index') #index로 보내줌
    return render(request, 'create.html', {'jss_form':jss_form}) #create.html에 jss_form의 정보를 담아 화면 정송

def create_comment(request): #create_comment 함수 정의
    comment_form = CommentForm(request.POST) #POST 방식으로 온 CommentForm이 comment_form에 저장
    if comment_form.is_valid(): #들어온 데이터 유효성 검사에 문제가 없다면
        temp_form = comment_form.save(commit=False) #잠시 저장되기 전 저장 지연 
        temp_form.author = request.user #request.user를 temp_form.author를 넣어줌
        temp_form.Jasosseol = Jasoseol.objects.get(pk=jss_id) #Jasoseol의 특정 객체 temp_form.Jasosseol에 적용
        temp_form.save() #temp_form 저장
        return redirect('detail', jss_id) #detail로 보내줌

def delete_comment(request, jss_id, comment_id): #jss_id와 comment_id를 담은 delete_comment 함수 정의
   my_comment = Comment.objects.get(pk=comment_id) #comment_id를 가진 객체를 my_comment에 적용
   if request.user == my_comment.author: #만약 request.user와 my_comment.author가 같다면
       my_comment.delete() #my_comment.delete를 지워준다
       return redirect('detail', jss_id) #detail 페이지로 보냄

   else:
       raise PermissionDenied #아니라면 권한 위반 메세지 출력



    