from django.shortcuts import render
from rest_framework import generics

from api.models import Pessoa
from api.serializers import PessoaSerializer


class ListarCriarPessoaView(generics.ListCreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class EditarBuscarDeletarPessoaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


