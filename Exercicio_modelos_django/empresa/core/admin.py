from django.contrib import admin
from .models import Cliente
from .models import Venda
from .models import Produto
from .models import ItemVenda
from .models import Fornecedor
from .models import Pedido
from .models import ItemPedido


admin.site.register(Cliente)
admin.site.register(Venda)
admin.site.register(Produto)
admin.site.register(ItemVenda)
admin.site.register(Fornecedor)
admin.site.register(Pedido)
admin.site.register(ItemPedido)



# Register your models here.
