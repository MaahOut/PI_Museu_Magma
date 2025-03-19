from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class HistoricoEstoque(models.Model):
    TIPO_CHOICES = [
        ('entrada', 'Entrada de Estoque'),
        ('venda', 'Venda'),
        ('ajuste', 'Ajuste de Estoque'),
        ('alteracao_preco', 'Alteração de Preço'),
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    quantidade = models.IntegerField()
    valor_inicial_estoque = models.IntegerField()
    valor_final_estoque = models.IntegerField()
    preco_anterior = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    preco_novo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    nome_cliente = models.CharField(max_length=100, null=True, blank=True)  # Novo campo
    cpf_cliente = models.CharField(max_length=14, null=True, blank=True)   # Novo campo
    cnpj_cliente = models.CharField(max_length=18, null=True, blank=True)  # Novo campo
    registro_venda = models.CharField(max_length=50, null=True, blank=True)  # Novo campo
    data_movimentacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.produto.nome} - {self.data_movimentacao}"