from django.contrib import admin
from upload.models import Data,Second_Data,New_Second_Data


class dataAdmin(admin.ModelAdmin):
    list_display = ['Class', 'name', 'num', 'content', 'handle']
admin.site.register(Data,dataAdmin)




class SecondAdmin(admin.ModelAdmin):

    list_display = ["Second_Class","Second_name","Second_num","Second_absenteeism"]

admin.site.register(Second_Data,SecondAdmin)



class N_SencondAdmin(admin.ModelAdmin):
    list_display = ['Class','name', 'num', 'content', 'handle']



admin.site.register(New_Second_Data,N_SencondAdmin)