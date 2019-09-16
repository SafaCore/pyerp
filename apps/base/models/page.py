# Librerias Django
from django.db import models
from django.urls import reverse

# Librerias de terceros
from apps.base.models import PyFather


class PyPage(PyFather):
    title = models.CharField('Nombre', max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    keywords = models.CharField('Keywords', max_length=20, blank=True)

    def get_absolute_url(self):
        return reverse('base:page-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.title)
