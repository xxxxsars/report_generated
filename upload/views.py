from django.http import  HttpResponse
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from upload.forms import UploadFileForm
from django.contrib import auth

from django.contrib.auth.models import User
import re
from upload.trans import *
from upload.secondary import *
from upload.models import Data,Second_Data,New_Second_Data
import os


def i(request):
    if request.user.is_authenticated():
        username = request.user.username
        return  render_to_response("index.html",locals())
    else:
        error="請重新登錄！"
        return render_to_response("error.html",locals())


def index(request):
    try:
        if request.method == 'POST':
            a=request.POST
            form = UploadFileForm(request.POST, request.FILES)
            username = request.user.username
            if form.is_valid() :
                #如果post有資料 先清除db上的資料
                Data.objects.all().delete()
                c = {'form': form}

                #擷取使用者輸入的資料呈現到表單上
                year = request.POST["year"]
                month = request.POST["month"]
                day = request.POST["day"]

                content_year  = request.POST["content_year"]
                content_month = request.POST["content_month"]
                filename = request.FILES['file'].name


                #判斷上傳的副檔名是否為xlsx 若是的話既係動作，不是的話傳回錯誤訊息並返回上傳頁面
                if re.search(r".+\.(.+)",filename).group(1)=="xlsx":
                    handle_uploaded_file(request.FILES['file'])
                    a  = Auto(filename,content_year,content_month)
                    a.run()

                    C_all = sorted(set(Data.objects.values_list("Class",flat=True)))
                    sorted(C_all)
                    datas = []
                    for c in C_all:
                        d =Data.objects.filter(Class=c)
                        datas.append(d)


                    #當處理完畢刪除上傳的檔案
                    os.remove("upload/"+filename)

                    return render(request, 'table.html', locals())
                else:
                    error = "上傳錯誤，請上傳xlsx的excel檔案"
                    return render(request, 'upload.html', locals())
        else:
            form = UploadFileForm()
            username = request.user.username
            c = {'form': form}

        return render(request,'upload.html', c)
    except:
        return render_to_response("error.html",locals())


def second_index(request):
    try:
        if request.method == 'POST':
            a=request.POST
            form = UploadFileForm(request.POST, request.FILES)
            username = request.user.username
            if form.is_valid() :
                #如果post有資料 先清除db上的資料
                Second_Data.objects.all().delete()
                New_Second_Data.objects.all().delete()
                c = {'form': form}

                #擷取使用者輸入的資料呈現到表單上
                year = request.POST["year"]
                month = request.POST["month"]
                day = request.POST["day"]

                content_year  = request.POST["content_year"]
                content_month = request.POST["content_month"]
                filename = request.FILES['file'].name


                #判斷上傳的副檔名是否為xlsx 若是的話既係動作，不是的話傳回錯誤訊息並返回上傳頁面
                if re.search(r".+\.(.+)",filename).group(1)=="xlsx":
                    handle_uploaded_file(request.FILES['file'])
                    a  = Data_tans(filename,content_year,content_month)
                    a.run()
                    a.trans_data()

                    C_all = sorted(set(New_Second_Data.objects.values_list("Class",flat=True)))
                    sorted(C_all)
                    datas = []
                    for c in C_all:
                        d =New_Second_Data.objects.filter(Class=c)
                        datas.append(d)


                    #當處理完畢刪除上傳的檔案
                    os.remove("upload/"+filename)
                    return render(request, 'table.html', locals())
                else:
                    error = "上傳錯誤，請上傳xlsx的excel檔案"
                    return render(request, 'upload.html', locals())
        else:
            form = UploadFileForm()
            username = request.user.username
            c = {'form': form}

        return render(request,'upload.html', c)
    except:
        return render_to_response("error.html", locals())



def handle_uploaded_file(file):
#    logging.debug("upload_here")
    if file:
        destination = open('upload/'+file.name, 'wb+')
        #destination = open('/tmp', 'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/index/')

    #有username就取得
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render(request,'login.html',locals())

def logout(request):
    auth.logout(request)
    return  HttpResponseRedirect('/login/')

def register(request):
    if request.method == 'POST':
        username = request.POST.get("username",'')
        password =request.POST.get("password",'')
        token = request.POST.get("yfms_token",'')

        users = User.objects.values_list()
        all_user = []
        for user in users:
            all_user.append(str(user[4]))
        if username not in all_user:
            if token=="3692679":
                user = User.objects.create_user(username, 'example@example.com', password)
                scuess = "註冊成功3秒後轉入登入頁...."
                return render(request, "register.html", locals())
            else:
                error="授權碼錯誤！"
                return render(request,"register.html",locals())
        else:
            error = "此帳號已註冊過！"
            return render(request, "register.html", locals())
    else:
        return render(request,"register.html",locals())



def redict(request):
    return HttpResponseRedirect('/login/')