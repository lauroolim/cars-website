# sistema/urls.py
from django.urls import path
from veiculo.views import ListarVeiculos, FotoVeiculo

urlpatterns = [
    path('listar/', ListarVeiculos.as_view(), name='listar-veiculos'),
    path('upload-foto/', FotoVeiculo, name='upload-foto'),
]
