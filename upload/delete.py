import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'report.settings')
import django

django.setup()



from upload.models import Data


import collections


C_all = (set(Data.objects.values_list("Class",flat=True)))



aa= []
for c in C_all:
    for c in C_all:
        datas =Data.objects.filter(Class=c)

        aa.append(datas)


for a in aa:
    print(a[0].Class)
    for c in a:
        if len(a)<=12:
            print(c.name)
        print("補"*(12-len(a)))