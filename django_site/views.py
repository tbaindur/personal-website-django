from django.http import HttpResponse


def ping(request):
    return HttpResponse("<h1>Ping Received for tejasbaindur.com</h1>")