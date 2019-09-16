# Librerias Future
from __future__ import unicode_literals

# Librerias Django
from django.shortcuts import HttpResponse, redirect, render

# Librerias en carpetas locales
from ...base.models.base_config import BaseConfig


def IndexEasy(request):
    count_pw = BaseConfig.objects.all().count()
    if count_pw > 0:
        return render(request, 'base/index.html')
    else:
        return render(request, 'base/install.html')
