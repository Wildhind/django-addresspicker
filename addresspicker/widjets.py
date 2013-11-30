from django.conf import settings
from django.forms import widgets
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.forms.util import flatatt
from django.template.loader import render_to_string
from django.utils.html import conditional_escape


class AddressPickerWidget(widgets.TextInput):
    class Media:
        def __init__(self):
            pass

        css = {'all': (
            settings.STATIC_URL + 'addresspicker/css/style.css',
            'http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css'
        ), }
        js = (
            'http://code.jquery.com/jquery-1.9.1.js',
            'http://code.jquery.com/ui/1.10.3/jquery-ui.js',
            'https://maps.google.com/maps/api/js?sensor=true',
            settings.STATIC_URL + 'addresspicker/js/jquery.ui.addresspicker.js',
            settings.STATIC_URL + 'addresspicker/js/init.js',
        )

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            final_attrs['value'] = force_unicode(self._format_value(value))
        return mark_safe(render_to_string('addresspicker/map.html', {
            'final_attrs': flatatt(final_attrs),
            'value': conditional_escape(force_unicode(value)),
            'latlng': conditional_escape(force_unicode(value)).split(','),
            'id': final_attrs['id']
        }))