from .models import RequestLog


class RequestLogMiddleware(object):
    def process_request(self, request):
        RequestLog.objects.create(path=request.path)
        return None
