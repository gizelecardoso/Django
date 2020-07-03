from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class CPF(models.Model):
    numero = models.CharField(max_length=15)
    data_exp = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.numero

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False)
    endereco = models.CharField(max_length=100, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()

    cpf = models.OneToOneField(CPF, on_delete=models.CASCADE, null=True, blank=True)

    departamentos = models.ManyToManyField(Departamento, blank=True)

    fotos = models.ImageField(upload_to='clientes_fotos')

    def __str__(self):
        return self.nome

class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    descricao = models.CharField(max_length=80)
    #Foreign Key é o relacionamento OneToMany - vários telefones para um cliente, um cliente tem vários telefones
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao + ' - ' + self.numero
