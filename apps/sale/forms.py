"""Formularios del modulo sale
"""
# Django Library
# Librerias Django
from django.forms import HiddenInput, ModelForm, NumberInput, TextInput

# Thirdparty Library
# Librerias de terceros
from dal import autocomplete

# Localfolder Library
# Librerias en carpetas locales
from .models import PySaleOrder, PySaleOrderDetail


# ========================================================================== #
class SaleOrderForm(ModelForm):
    """Formulario para agregar y/o editar ordenes de compra
    """
    class Meta:
        model = PySaleOrder
        fields = [
            'partner_id',
            'description',
        ]
        labels = {
            'partner_id': 'Cliente',
            'description': 'Descripción',
        }
        widgets = {
            'partner_id': autocomplete.ModelSelect2(
                url='PyPartner:autocomplete',
                attrs={
                    'class': 'form-control',
                    'data-placeholder': 'Seleccione un cliente ...',
                    'style': 'width: 100%',
                },
            ),
            'description': TextInput(
                attrs={
                    'class': 'form-control',
                    'data-placeholder': 'Descripción del presupuesto ...',
                    'style': 'width: 100%',
                },
            ),
        }


# ========================================================================== #
class SaleOrderDetailForm(ModelForm):
    """Formulario para agregar y/o editar ordenes de compra
    """
    class Meta:
        model = PySaleOrderDetail
        fields = [
            'sale_order',
            'product',
            'description',
            'quantity',
            # 'measure_unit',
            # 'product_tax',
            'amount_untaxed',
            'discount',
            # 'amount_total',
        ]
        labels = {
            'product': 'Producto',
            'description': 'Descripción',
            'quantity': 'Cantidad',
            # 'measure_unit': 'Unidad',
            # 'product_tax': 'Impuesto',
            'amount_untaxed': 'Precio',
            'discount': 'Descuento',
            # 'amount_total': 'Sub total',
        }
        widgets = {
            'sale_order': HiddenInput(),
            'product': autocomplete.ModelSelect2(
                url='sale:product-autocomplete',
                forward=('sale_order',),
                attrs={
                    'class': 'form-control',
                    'data-placeholder': 'Seleccione un producto ...',
                    'style': 'width: 100%',
                },
            ),
            'description': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripción del producto ...',
                    'style': 'width: 100%',
                },
            ),
            'quantity': NumberInput(
                attrs={
                    'class': 'form-control',
                    'data-placeholder': 'Cantidad del producto ...',
                    'style': 'width: 100%',
                },
            ),
            # 'measure_unit': autocomplete.ModelSelect2(
            #     url='measure-unit-autocomplete',
            #     attrs={
            #         'class': 'form-control',
            #         'data-placeholder': 'Seleccione un unidad ...',
            #         'style': 'width: 100%',
            #     },
            # ),
            # 'product_tax': autocomplete.ModelSelect2(
            #     url='PyTax:autocomplete',
            #     attrs={
            #         'class': 'form-control',
            #         'data-placeholder': 'Seleccione un Impuesto ...',
            #         'style': 'width: 100%',
            #     },
            # ),
            'amount_untaxed': NumberInput(
                attrs={
                    'class': 'form-control',
                    'data-placeholder': 'Precio del producto ...',
                    'style': 'width: 100%',
                },
            ),
            'discount': NumberInput(
                attrs={
                    'class': 'form-control',
                    'data-placeholder': 'Descuento ...',
                    'style': 'width: 100%',
                },
            ),
            # 'amount_total': NumberInput(
            #     attrs={
            #         'class': 'form-control',
            #         'data-placeholder': 'Sub total ...',
            #         'style': 'width: 100%',
            #     },
            # ),
        }
