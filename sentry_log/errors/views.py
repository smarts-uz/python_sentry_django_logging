from django.shortcuts import render


def errors_index(request):
    raise Exception('testing exception')
    return render(request, 'index.html', {})