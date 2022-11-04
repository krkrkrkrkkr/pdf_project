from django.shortcuts import render
from django.http import FileResponse, Http404

# Create your views here.
def home(request):
    try:
        return FileResponse(open('readme.pdf','rb'),content_type="application/pdf")
    except FileNotFoundError:
        raise Http404()

