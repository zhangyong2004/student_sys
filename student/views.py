
# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Student
from .forms import StudentForm

# 定义合成首页的方法index()，返回渲染的首页视图
def index(request):
    #1.首页index.html的学生数据
    students = Student.objects.all()

    #2.首页index.html的form数据
    if request.method == 'POST': #post方式提交数据
        form = StudentForm(request.POST) #创建post方式的表单对象，包含表单中填入的数据
        if form.is_valid():
            form.save() #保存数据到数据库
            return HttpResponseRedirect(reverse('index')) #重定向到首页
    else:  #get方式访问form页面
        form = StudentForm() #创建get方式的表单对象，空的表单页面

    return render(request,'index.html',context={'students':students,'form':form})