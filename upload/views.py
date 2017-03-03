from django.http import  HttpResponse
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from upload.forms import UploadFileForm
import re
from upload.trans import *
from upload.secondary import *
from upload.models import Data,Second_Data,New_Second_Data
import os


def i(request):
    return  render_to_response("index.html",locals())


def index(request):
    try:
        if request.method == 'POST':
            a=request.POST
            form = UploadFileForm(request.POST, request.FILES)

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

            c = {'form': form}

        return render(request,'upload.html', c)
    except:
        return render_to_response("error.html",locals())


def second_index(request):
    try:
        if request.method == 'POST':
            a=request.POST
            form = UploadFileForm(request.POST, request.FILES)

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
