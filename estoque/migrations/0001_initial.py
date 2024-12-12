# Generated by Django 5.1.4 on 2024-12-12 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('cnpj', models.CharField(max_length=14, unique=True)),
                ('telefone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('codigo', models.CharField(max_length=15, unique=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade_estoque', models.IntegerField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('categorias', models.ManyToManyField(to='estoque.categoria')),
                ('fornecedor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='estoque.fornecedor')),
            ],
        ),
    ]