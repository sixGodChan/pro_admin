from django.template import Library
from types import FunctionType
from django.forms.models import ModelChoiceField
from sixgod.service import v1
from django.urls import reverse

register = Library()


def add_edit_page(form):
    for item in form:
        row = {'item': None, 'is_popup': False, 'popup_url': None}
        if isinstance(item.field, ModelChoiceField) and item.field.queryset.model in v1.site._registry:
            app_label = item.field.queryset.model._meta.app_label
            model_name = item.field.queryset.model._meta.model_name
            url_name = '{0}:{1}_{2}_add'.format(v1.site.namespace, app_label, model_name)
            url = reverse(url_name)
            row['is_popup'] = True
            row['popup_url'] = '{0}?popup_id={1}'.format(url, item.auto_id)
        row['item'] = item
        yield row


@register.inclusion_tag('sg/md_add_edit.html')
def func(form):
    ae_obj = add_edit_page(form)
    return {'ae_obj': ae_obj}
