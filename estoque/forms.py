from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Categoria, Fornecedor, Produto
import re

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'codigo', 'descricao', 'preco', 'quantidade_estoque', 'fornecedor', 'categorias']
    
    categorias = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Categorias"
    )

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if len(nome) < 3:
            raise forms.ValidationError("O nome do produto deve ter pelo menos 3 caracteres.")
        return nome

    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')
        if not codigo.isalnum():
            raise forms.ValidationError("O código do produto deve conter apenas letras e números (sem espaços ou caracteres especiais).")
        return codigo

    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco <= 0:
            raise forms.ValidationError("O preço do produto deve ser maior que zero.")
        return preco

    def clean_quantidade_estoque(self):
        quantidade_estoque = self.cleaned_data.get('quantidade_estoque')
        if quantidade_estoque < 0:
            raise forms.ValidationError("A quantidade em estoque deve ser um número inteiro maior ou igual a zero.")
        return quantidade_estoque

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
    
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        categoria = Categoria.objects.filter(nome=nome)

        if categoria:
            raise forms.ValidationError("Já existe uma categoria com esse nome.")
        return nome

# class CategoriaForm(forms.Form):
#     nome = forms.CharField(max_length=250, label="Nome")

#     def clean_nome(self):
#         nome = self.cleaned_data.get('nome')
#         categoria = Categoria.objects.filter(nome=nome)

#         if categoria:
#             raise forms.ValidationError("Já Existe uma Categoria com Esse Nome.")
#         return nome

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'cnpj', 'telefone', 'email']
    
    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        if cnpj and not re.match(r'^\d{14}$', cnpj):
            raise forms.ValidationError("O CNPJ Deve Conter Apenas 14 Números.")
        return cnpj
    
    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if telefone and not re.match(r'^\d{10,11}$', telefone):
            raise forms.ValidationError("O Telefone Deve Conter Apenas Números, com 10 ou 11 Dígitos.")
        return telefone
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not re.match(r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b$', email):
            raise forms.ValidationError("Digite um Endereço de E-mail Válido.")
        return email

# class FornecedorForm(forms.Form):
#     nome = forms.CharField(max_length=250, label="Nome")
#     cnpj = forms.CharField(max_length=14, label="CNPJ")
#     telefone = forms.CharField(max_length=11, label="Telefone")
#     email = forms.EmailField(max_length=254)

#     def clean_cnpj(self):
#         cnpj = self.cleaned_data.get('cnpj')
#         if cnpj and not re.match(r'^\d{14}$', cnpj):
#             raise forms.ValidationError("O CNPJ Deve Conter Apenas 14 Números.")
#         return cnpj
    
#     def clean_telefone(self):
#         telefone = self.cleaned_data.get('telefone')
#         if telefone and not re.match(r'^\d{10,11}$', telefone):
#             raise forms.ValidationError("O Telefone Deve Conter Apenas Números, com 10 ou 11 Dígitos.")
#         return telefone
    
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if email and not re.match(r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b$', email):
#             raise forms.ValidationError("Digite um Endereço de E-mail Válido.")
#         return email

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label="Nome")
    last_name = forms.CharField(max_length=30, required=True, label="Sobrenome")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
