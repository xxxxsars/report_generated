from django import forms


class UploadFileForm(forms.Form):
    year = forms.CharField(max_length=50 ,label="製表年份")
    month = forms.CharField(max_length=50,label="製表月份")
    day = forms.CharField(max_length=50,label="製表日期")
    file  = forms.FileField(label="上傳檔案")

    content_year = forms.CharField(max_length=50,label="懲處學生資料年份")
    content_month = forms.CharField(max_length=50,label="懲處學生資料月份")