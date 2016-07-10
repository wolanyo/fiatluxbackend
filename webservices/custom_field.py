# -*- coding: utf-8 -*-


class CustomDateField(forms.DateField):
  def __init__(self, *args, **kwargs):
    kwargs.setdefault('input_formats', ("%d.%m.%Y",))
    super(CustomDateField, self).__init__(*args, **kwargs)


class CustomTimeField(forms.DateField):
  def __init__(self, *args, **kwargs):
    kwargs.setdefault('input_formats', ("%H:%M",))
    super(CustomDateField, self).__init__(*args, **kwargs)