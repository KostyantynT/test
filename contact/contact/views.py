from django.views import generic

from .models import ContactInfo
from .models import RequestLog


class ContactView(generic.DetailView):
    model = ContactInfo

    def get_object(self):
        return ContactInfo.objects.all()[0]


class RequestsView(generic.ListView):
    model = RequestLog
    queryset = RequestLog.objects.all()[:10]
