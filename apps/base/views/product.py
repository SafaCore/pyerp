# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias de terceros
# from apps.sale.models import PySaleOrderDetail
from dal import autocomplete

# Librerias en carpetas locales
from ..models import PyProduct

PRODUCT_FIELDS = [
    {'string': _("Code"), 'field': 'code'},
    {'string': _("Bar Code"), 'field': 'bar_code'},
    {'string': _("Name"), 'field': 'name'},
    {'string': _("UOM"), 'field': 'uom_id'},
    {'string': _("Tax"), 'field': 'tax_id'},
    {'string': _("Category"), 'field': 'category_id'},
    {'string': _("Web Category"), 'field': 'web_category_id'},
    {'string': _("Price"), 'field': 'price'},
    {'string': _("Cost"), 'field': 'cost'},
    {'string': _("Type"), 'field': 'type'},
    {'string': _("Created On"), 'field': 'created_on'},
    {'string': _("Descriptions"), 'field': 'description'},

]

LEAD_FIELDS_SHORT = [
    'name',
    'uom_id',
    'category_id',
    'tax_id',
    'web_category_id',
    'code',
    'bar_code',
    'price',
    'cost',
    'type',
    'web_active',
    'img',
    'description',
]


class ProductListView(LoginRequiredMixin, ListView):
    model = PyProduct
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Productos'
        context['detail_url'] = 'base:product-detail'
        context['add_url'] = 'base:product-add'
        context['fields'] = PRODUCT_FIELDS
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = PyProduct
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:products', 'name': 'Productos'}]
        context['detail_name'] = 'Producto: %s' % context['object'].name
        context['update_url'] = 'base:product-update'
        context['delete_url'] = 'base:product-delete'
        context['fields'] = PRODUCT_FIELDS
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = PyProduct
    fields = LEAD_FIELDS_SHORT
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear producto'
        context['breadcrumbs'] = [{'url': 'base:products', 'name': 'Productos'}]
        context['back_url'] = reverse('base:products')
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = PyProduct
    fields = LEAD_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:products', 'name': 'Productos'}]
        context['back_url'] = reverse('base:product-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteProduct(self, pk):
    product = PyProduct.objects.get(id=pk)
    product.delete()
    return redirect(reverse('base:products'))
