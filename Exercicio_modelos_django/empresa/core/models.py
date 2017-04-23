from django.db import models
from decimal import Decimal
import decimal

class Cliente(models.Model):
    cpf = models.CharField(max_length=14)
    nome = models.CharField(max_length=30)
    endereco= models.CharField(max_length=35)
    complemento= models.CharField(max_length=50)
    cidade= models.CharField(max_length=25)
    estado= models.CharField(max_length=2)
    cep= models.CharField(max_length=8)
    FoneResidencial = models.CharField(max_length=15)
    FoneTrabalho= models.CharField(max_length=15)
    RendaFamiliar= models.DecimalField(max_digits=50,decimal_places=2)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    CodigoVenda = models.AutoField(primary_key=True)
    DataVenda = models.DateField()
    ValorTotal = models.DecimalField(max_digits=10,decimal_places=2)
    CodigoCliente = models.CharField(max_length=14)
    def __str__(self):
        return str(self.CodigoVenda)



class Produto(models.Model):
    CodigoProduto = models.IntegerField()
    NomeProduto = models.CharField(max_length=35)
    Quantidade = models.IntegerField()
    MinQuantidade = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return str(self.CodigoProduto)+' - '+self.NomeProduto

class ItemVenda(models.Model):
    CodigoVenda = models.IntegerField(default=0)
    CodigoProduto = models.IntegerField(default=0)
    PrecoUnitario = models.DecimalField(max_digits=10,decimal_places=2)
    Quantidade = models.IntegerField()

    def save(self, *args, **kwargs):
        venda = Venda.objects.get(CodigoVenda=self.CodigoVenda)
        venda.ValorTotal+=Decimal(self.PrecoUnitario)*self.Quantidade
        venda.save()
        produto = Produto.objects.get(CodigoProduto=self.CodigoProduto)
        produto.Quantidade-=self.Quantidade
        produto.save()

        super(ItemVenda, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.CodigoVenda)

class Fornecedor(models.Model):
    Cnpj = models.CharField(max_length=20)
    Nome = models.CharField(max_length=30)
    Endereco = models.CharField(max_length=35)
    Complemento = models.CharField(max_length=50)
    Cidade = models.CharField(max_length=25)
    Estado =models.CharField(max_length=2)
    Cep =models.CharField(max_length=8)
    Fone = models.CharField(max_length=15)
    Responsavel = models.CharField(max_length=30)
    Website = models.CharField(max_length=80)
    def __str__(self):
        return self.Cnpj

class Pedido(models.Model):
    Codigo = models.AutoField(primary_key=True)
    DataPedido = models.DateField()
    DataRecebimento = models.DateField()
    PrecoTotal = models.DecimalField(max_digits=10,decimal_places=2)
    CodigoFornecedor = models.CharField(max_length=20)
    def __str__(self):
        return str(self.Codigo)

class ItemPedido(models.Model):
    CodigoPedido = models.IntegerField()
    CodigoProduto = models.IntegerField()
    PrecoUnitario = models.DecimalField(max_digits=10,decimal_places=2)
    Quantidade = models.IntegerField()

    def save(self, *args, **kwargs):
        pedido = Pedido.objects.get(Codigo=self.CodigoPedido)
        pedido.PrecoTotal+=Decimal(self.PrecoUnitario)*self.Quantidade
        pedido.save()

        super(ItemPedido, self).save(*args, **kwargs)

    def __str__(self):

        return str(self.CodigoPedido)





# Create your models here.
