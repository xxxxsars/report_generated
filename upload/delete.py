import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'report.settings')
import django

django.setup()



from upload.models import Data
from django.contrib.auth.models import User


import collections


C_all = (set(Data.objects.values_list("Class",flat=True)))




users = User.objects.values_list()

all_user = []

for user in users:
    all_user.append(str(user[4]))



for i,u in enumerate(all_user):
    a = User.objects.get(username=u)
