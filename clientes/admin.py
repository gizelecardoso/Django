from django.contrib import admin
from .models import Cliente, Telefone, CPF, Departamento

class ClienteAdmin(admin.ModelAdmin):
    #fields = ('nome', 'endereco', 'salario')
    list_display = ('id','nome', 'endereco', 'email')
    list_filter = ('departamentos',)
    search_fields = ('id', 'nome', 'departamentos__nome')


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Departamento)