from django.shortcuts import redirect


def guest(get_response):
    # One-time configuration and initialization.
    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if not request.user.is_authenticated:
            return get_response(request)

        return redirect('website:home')
        # Code to be executed for each request/response after
        # the view is called.

    return middleware
