from django.urls import path
from .views import index,create,detail,delete,update,my_index, create_comment,delete_comment #함수 등록

#경로 연결(경로,사용할 함수, 이름)
urlpatterns =[
    path('',index, name="index"),
    path('my_index', my_index, name="my_index"),
    path('create/', create, name="create"),
    path('detail/<int:jss_id>', detail, name="detail"), #숫자형식으로 jss_id를 detail에 보내줌
    path('delete/<int:jss_id>', delete, name="delete"), #숫자형식으로 jss_id를 delete에 보내줌
    path('update/<int:jss_id>', update, name="update"), #숫자형식으로 jss_id를 update에 보내줌

    #comment#
    path('create_comment/<int:jss_id>/', create_comment, name="create_comment"),
    path('delete_comment/<int:jss_id>/<int:comment_id>/', delete_comment, name="delete_comment"),
]