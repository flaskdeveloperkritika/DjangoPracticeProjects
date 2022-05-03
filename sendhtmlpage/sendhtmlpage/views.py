from django.shortcuts import render


def send_html(request):
    return render(request, 'home.html')