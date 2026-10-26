"""A series of handlers will process requests. Each handler can deal with the
request, and if it can't, then the next handler will deal with it """

# option 1, to contract new service
# option 2, for technical issues
# option 3, to speak with an agent

# each request will be handled by the responsible department


class Handler:
    """base handler of the chain, keeps a reference to the next handler"""
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        """passes the request to the successor, or returns None at the end of the chain"""
        if self._successor:
            return self._successor.handle_request(request)
        return None


class SalesDepartment(Handler):
    """handles option 1 (contracting a new service)"""
    def handle_request(self, request):
        if request == '1':
            return 'Sales department handled the request'
        return super().handle_request(request)


class TechnicalIssues(Handler):
    """handles option 2 (technical issues)"""
    def handle_request(self, request):
        if request == '2':
            return 'The tech department handled the request'
        return super().handle_request(request)


class SpeakToOperator(Handler):
    """handles option 3 (speaking with an agent)"""
    def handle_request(self, request):
        if request == '3':
            return 'An agent handled the request'
        return super().handle_request(request)


if __name__ == "__main__":
    handler1 = SalesDepartment(TechnicalIssues(SpeakToOperator()))
    print(handler1.handle_request('1'))
    print(handler1.handle_request('2'))
    print(handler1.handle_request('3'))
    print(handler1.handle_request('unknown request'))
