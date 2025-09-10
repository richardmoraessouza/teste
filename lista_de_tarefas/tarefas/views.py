from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Tarefa_usuario

def lista(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        descricao = request.POST.get('descricao', '').strip()
        if nome and descricao:
               Tarefa_usuario.objects.create(nome=nome, descricao=descricao)
        return redirect('lista')

    tarefas = Tarefa_usuario.objects.all().order_by('-id')
    context = { 'tarefas': tarefas}
    return render(request, 'mostrar_tarefas/index.html', context)


def api_tarefas(request):
    tarefas_queryset = Tarefa_usuario.objects.all().order_by('id')
    tarefas = [
        {
            'id': tarefa.id,
            'nome': tarefa.nome,
            'descricao': tarefa.descricao,
        }
        for tarefa in tarefas_queryset
    ]
    return JsonResponse({'tarefas': tarefas})