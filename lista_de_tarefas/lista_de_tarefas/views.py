from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Essa é a rota de teste!")