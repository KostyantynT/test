from django import template
register = template.Library()


@register.filter('is_File')
def is_File(form_field_obj):
    return form_field_obj.field.widget.__class__.__name__ == "FileInput"