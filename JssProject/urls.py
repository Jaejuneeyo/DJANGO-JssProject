
from django.contrib import admin
from django.urls import path
from main.views import index,create


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name="index"),
    path('create/', create, name="create"),
]
