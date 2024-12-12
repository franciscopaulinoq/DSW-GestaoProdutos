from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=250)
    cnpj = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=250)
    codigo = models.CharField(max_length=15, unique=True)
    descricao = models.TextField(null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    categorias = models.ManyToManyField(Categoria)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nome