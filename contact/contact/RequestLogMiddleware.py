from models import RequestLog


class RequestLogMiddleware(object):
    def process_request(self, request):
        log = RequestLog()
        log.path = request.path
        #assume it will be our rule for priority
        #if it will be necessary we will add here some logic
        log.priority = True
        log.save()
        return None
