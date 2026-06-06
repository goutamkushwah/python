from django.shortcuts import render


def say_hello(request):
    #return render(request, 'hello.html')
    #return HttpResponse('Hello World')
    return render(request, 'hello.html', {'name': 'Goutam'})