from django import forms
from django.db import models

class MyFormDateField(forms.DateField):
    def __init__(self, *args, **kwargs):
        # you still want %Y-%m-%d on the list as it's
        # what the javascript datepicker used by the admin
        # injects on the client side.
        d = dict(input_formats=('%d/%m/%y', '%d-%b-%y','%Y-%m-%d'))
        d.update(kwargs)
        super(MyFormDateField, self).__init__(*args, **d)

class MyModelDateField(models.DateField):
    def formfield(self, *args, **kwargs):
        d = dict(form_class=MyFormDateField)
        d.update(kwargs)
        return super(MyModelDateField, self).formfield(*args, **d)