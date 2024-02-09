from inertia import share
from django.conf import settings
from django.contrib import messages


def inertia_share(get_response):
  def middleware(request):
    share(request, 
      #messages = [m.message for m in messages.get_messages(request)],
      #app_name=settings.APP_NAME,
      #user_count=lambda: User.objects.count(), # evaluated lazily at render time
      #user=lambda: request.user, # evaluated lazily at render time
    )

    return get_response(request)
  return middleware

class InertiaShare(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        share(request,
              message =[m.message for m in messages.get_messages(request)])
        response = self.get_response(request)
        
        return response