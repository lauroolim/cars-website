from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.core.files.storage import FileSystemStorage
from veiculo.models import Veiculo

class ListarVeiculos(ListView):
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'

def FotoVeiculo(request):
    if request.method == 'POST' and request.FILES['foto']:
        foto = request.FILES['foto']
        fs = FileSystemStorage()
        filename = fs.save(foto.name, foto)
        uploaded_file_url = fs.url(filename)
        return render(request, 'veiculo/foto_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'veiculo/foto_upload.html')
