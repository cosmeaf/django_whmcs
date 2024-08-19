from django.shortcuts import render, HttpResponse, Http404
import os
from .middleware import get_subdomain, get_hostname

def render_project(request):
    subdomain = get_subdomain(request)
    hostname = get_hostname(request)

    # Verifique se é o domínio principal (sem subdomínio)
    if hostname == 'projetodesenvolve.duckdns.org':
        return render(request, 'index.html')

    # Diretório do projeto deve ser acessado através do link simbólico
    project_directory = os.path.join('/var/www/', subdomain)
    index_path = os.path.join(project_directory, 'index.html')

    # Debugging: Verificar o caminho
    print(f"Verificando o caminho: {index_path}")

    if os.path.exists(index_path):
        with open(index_path, 'r') as file:
            content = file.read()
        return HttpResponse(content)

    # Se o arquivo index.html não for encontrado, levanta uma exceção 404
    return custom_404_view(request)


def home_view(request):
    return render(request, 'index.html')

def contact_view(request):
    return render(request, 'contact.html')

def login_view(request):
    return render(request, 'login.html')

def about_view(request):
    return render(request, 'about.html')

def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)
