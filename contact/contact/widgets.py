import re
import uuid

from django.forms.widgets import  MultiWidget, to_current_timezone
from django.forms.widgets import DateTimeInput, Media
from django.utils.translation import ugettext as _
from datetime import datetime
from django.utils import translation
from django.utils.safestring import mark_safe

I18N = """
$.fn.datetimepicker.dates['en'] = {
    days: %s,
    daysShort: %s,
    daysMin: %s,
    months: %s,
    monthsShort: %s,
    meridiem: %s,
    suffix: %s,
    today: %s
};
"""

datetimepicker_options = """
    format : '%s',
    startDate : '%s',
    endDate : '%s',
    weekStart : %s,
    daysOfWeekDisabled : %s,
    autoclose : %s,
    startView : %s,
    minView : %s,
    maxView : %s,
    todayBtn : %s,
    todayHighlight : %s,
    minuteStep : %s,
    pickerPosition : '%s',
    showMeridian : %s,
    language : '%s',
"""

dateConversion = {
    'P': '%p',
    'ss': '%S',
    'ii': '%M',
    'hh': '%H',
    'HH': '%I',
    'dd': '%d',
    'mm': '%m',
    #'M' :  '%b',
    #'MM' : '%B',
    'yy': '%y',
    'yyyy': '%Y',
}


class DateTimeWidget(MultiWidget):

    def __init__(self, attrs=None, options=None):
        if attrs is None:
            attrs = {'readonly': ''}

        if options is None:
            options = {}

        self.option = ()
        self.option += (options.get('format', 'dd/mm/yyyy hh:ii'),)
        self.option += (options.get('startDate', ''),)
        self.option += (options.get('endDate', ''),)
        self.option += (options.get('weekStart', '0'),)
        self.option += (options.get('daysOfWeekDisabled', '[]'),)
        self.option += (options.get('autoclose', 'false'),)
        self.option += (options.get('startView', '2'),)
        self.option += (options.get('minView', '0'),)
        self.option += (options.get('maxView', '4'),)
        self.option += (options.get('todayBtn', 'false'),)
        self.option += (options.get('todayHighlight', 'false'),)
        self.option += (options.get('minuteStep', '5'),)
        self.option += (options.get('pickerPosition', 'bottom-right'),)
        self.option += (options.get('showMeridian', 'false'),)

        self.language = options.get('language', 'en')
        self.option += (self.language,)

        pattern = re.compile(r'\b(' + '|'.join(dateConversion.keys()) + r')\b')
        self.dataTimeFormat = self.option[0]
        self.format = pattern.sub(lambda x: dateConversion[x.group()],
                                  self.option[0])

        widgets = (DateTimeInput(attrs=attrs, format=self.format),)

        super(DateTimeWidget, self).__init__(widgets, attrs)

    def value_from_datadict(self, data, files, name):
        try:
            D = to_current_timezone(datetime.strptime(data[name], self.format))
        except ValueError:
            return ''
        else:
            return D

    def decompress(self, value):
        if value:
            value = to_current_timezone(value)
            return (value,)
        return (None,)

    def format_output(self, rendered_widgets):
        """
        Given a list of rendered widgets (as strings), it inserts an HTML
        linebreak between them.

        Returns a Unicode string representing the HTML for the whole lot.
        """

        js_options = datetimepicker_options % self.option
        id = uuid.uuid4().hex
        return '<div id="%s"  class="input-append date form_datetime">'\
               '%s'\
               '<span class="add-on"><i class="icon-th"></i></span>'\
               '</div>'\
               '<script type="text/javascript">'\
               '$("#%s").datetimepicker({%s});'\
               '</script>  ' % (id, rendered_widgets[0], id, js_options)

    def render(self, name, value, attrs=None):
        if self.is_localized:
            for widget in self.widgets:
                widget.is_localized = self.is_localized
        # value is a list of values, each corresponding to a widget
        # in self.widgets.
        if not isinstance(value, list):
            value = self.decompress(value)
        output = []
        final_attrs = self.build_attrs(attrs)
        id_ = final_attrs.get('id', None)
        try:
            widget_value = value[0]
        except IndexError:
            widget_value = None
        if id_:
            final_attrs = dict(final_attrs, id='%s_%s' % (id_, 0))

        output.append(self.widgets[0].render(name, widget_value, final_attrs))
        return mark_safe(self.format_output(output))

        def _media(self):
            js = ["js/bootstrap-datetimepicker.js"]
            if self.language != 'en':
                js.append("js/bootstrap-datetimepicker.js")

            return Media(
                css={
                    'all': ('css/datetimepicker.css',)
                },
                js=js
            )
        media = property(_media)
