from django.http import HttpResponse

from . import warning

# Create your views here.
def index(request):
    warning.warning()
    return HttpResponse("Success.")


