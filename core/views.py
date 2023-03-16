from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def home(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'core/pages/index.html',
    )
