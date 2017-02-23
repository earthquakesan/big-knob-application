from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

from pathlib import Path

# Create your views here.
def index(request):
    template = loader.get_template('root/index.html')
    _status = status(request)
    button_pushed = False
    if _status.content.decode("utf-8") == "0":
        button_pushed = True
    context = {
        "button_pushed": button_pushed
    }
    return HttpResponse(template.render(context, request))

def push(request):
    _push = Path("/tmp/button_pushed")
    if _push.exists():
        _push.unlink()
    else:
        _push.touch()
    return redirect("/index")

def status(request):
    _push = Path("/tmp/button_pushed")
    if _push.exists():
        # Healthy
        return HttpResponse("0")
    else:
        # Not healthy
        return HttpResponse("1")
