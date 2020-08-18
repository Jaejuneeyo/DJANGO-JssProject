from django import forms
from .models import Jasoseol,Comment

class JssForm(forms.ModelForm): #forms.ModelForm이 적용된 JssForm 생성

    class Meta:
        model = Jasoseol #자소설 모델 대응 
        fields = ('title', 'content', 'author') #폼에 나왔으면 하는 내용들 작성(제목,내용,시간)

    def __init__(self, *args, **kwargs): #내장함수 init 함수 커스텀
        super().__init__(*args, **kwargs) #ModelForm 안에 init 사용을 가능하게 함(안에 내용 참조 위함)
        self.fields['title'].label = "제목" #라벨을 제목으로 바꿈
        self.fields['content'].label ="자기소개서 내용" #content의 라벨을 자기소개서 내용으로 바꿈
        self.fields['title'].widget.attrs.update({ #폼 꾸며주는 부분 아래 부분
            'class' : 'jss_title',
            'placeholder':'제목',
        }) 
        self.fields['title'].widget.attrs.update({
            'class' : 'jss_content_form',
        })
class CommentForm(forms.ModelForm): #forms.ModelForm이 적용된 CommentForm 생성

    class Meta:
        model = Comment #comment와 model 대응
        fields = ('content',) #conent를 fields에 적용
