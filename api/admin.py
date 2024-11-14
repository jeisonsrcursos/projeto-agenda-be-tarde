from pyexpat import model

from django.contrib import admin

from api.models import Pessoa, Contato


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    model = Pessoa
    list_display = (
        'nome',
        'bairro',
        'cidade'
    )


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    model = Contato
    list_display = (
        'pessoa',
        'descricao'
    )
