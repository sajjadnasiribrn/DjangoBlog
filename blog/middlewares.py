from threading import current_thread

_requests = {}


def get_request():
    return _requests[current_thread()]


class GlobalRequestMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _requests[current_thread()] = request
        return self.get_response(request)
