from django.core.urlresolvers import reverse_lazy
from django.views import generic

from forms import ContactInfoForm
from models import ContactInfo
from models import RequestLog


class ContactView(generic.DetailView):
    model = ContactInfo
    
    def get_object(self):
        return ContactInfo.objects.all()[0]


class ContactUpdate(generic.UpdateView):
    form_class = ContactInfoForm
    success_url = reverse_lazy('contact_view')
    
    def get_object(self, queryset=None):
        return ContactInfo.objects.all()[0]

   
class RequestsView(generic.ListView):
    model = RequestLog
    queryset = RequestLog.objects.all()[:10]