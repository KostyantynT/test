from django.views import generic

from .models import ContactInfo

class ContactView(generic.DetailView):
    model = ContactInfo
    
    def get_object(self):
        return ContactInfo.objects.all()[0]