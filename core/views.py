from django.shortcuts import render

def home(request):
    contexto = {
        'mensaje': '¡Hola Django!',
        'autor': 'Frankyn',
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS']
    }
    return render(request, 'home.html', contexto)

def about(request):
    return render(request, 'about.html', {'autor': 'Frankyn'})
