"""A series of handlers will process requests. Each handler can deal with the
request, and if it can't, then the next handler will deal with it """

# option 1, to contract new service
# option 2, for technical issues
# option 3, to speak with an agent

# each request will be handled by the responsable department


class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        if self._successor:
            return self._successor.handle_request(request)
        return None


class SalesDepartment(Handler):
    def handle_request(self, request):
        if request == '1':
            return 'Sales department handled the request'
        else:
            return super().handle_request(request)


class TecnicalIssues(Handler):
    def handle_request(self, request):
        if request == '2':
            return 'The tech department handled the request'
        else:
            return super().handle_request(request)


class SpeakToOperator(Handler):
    def handle_request(self, request):
        if request == '3':
            return 'An agent handled the request'
        else:
            return super().handle_request(request)


handler1 = SalesDepartment(TecnicalIssues(SpeakToOperator()))
print(handler1.handle_request('1'))
print(handler1.handle_request('2'))
print(handler1.handle_request('3'))
print(handler1.handle_request('unknown request'))
