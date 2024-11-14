from django.urls import path

from api.views import ListarCriarPessoaView, EditarBuscarDeletarPessoaView

urlpatterns = [
    path(
        'pessoa/',
        ListarCriarPessoaView.as_view(),
        name='listar-criar-pessoa-view'
    ),
    path(
        'pessoa/<int:pk>',
        EditarBuscarDeletarPessoaView.as_view(),
        name='editar-buscar-deletar-pessoa-view'
    )
]