from django.shortcuts import render
from django.http import FileResponse, Http404
import os
from django.conf import settings
# Create your views here.
def home(request):
    try:
        filepath=os.path.join(settings.BASE_DIR,"readme.pdf")
        return FileResponse(open(filepath,'rb'),content_type="application/pdf")
    except FileNotFoundError:
        raise Http404()

