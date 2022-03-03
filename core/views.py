from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'curso': 'Curso Teste 1'
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')
