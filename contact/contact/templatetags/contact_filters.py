from django import template
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType

register = template.Library()


@register.filter('is_File')
def is_File(form_field_obj):
    return form_field_obj.field.widget.__class__.__name__ == "FileInput"


@register.simple_tag
def edit_link(obj):
    content_type = ContentType.objects.get_for_model(obj.__class__)
    return reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(obj.pk,))
