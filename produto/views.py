from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
from .models import Produto, HistoricoEstoque

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/lista_produtos.html', {'produtos': produtos})

@csrf_exempt
def adicionar_estoque(request, nome):
    produto = get_object_or_404(Produto, nome=nome)
    quantidade = int(request.POST.get('quantidade', 1))  # Quantidade recebida do formulário
    valor_inicial = produto.estoque
    produto.estoque += quantidade
    produto.save()
    HistoricoEstoque.objects.create(
        produto=produto,
        tipo='entrada',
        quantidade=quantidade,
        valor_inicial_estoque=valor_inicial,
        valor_final_estoque=produto.estoque
    )
    return JsonResponse({'status': 'success', 'estoque': produto.estoque})

@csrf_exempt
def registrar_venda(request, nome):
    produto = get_object_or_404(Produto, nome=nome)
    quantidade = int(request.POST.get('quantidade', 0))
    nome_cliente = request.POST.get('nomeCliente', '')
    cpf_cliente = request.POST.get('cpfCliente', '')
    cnpj_cliente = request.POST.get('cnpjCliente', '')
    registro_venda = request.POST.get('registroVenda', '')

    if quantidade > 0 and produto.estoque >= quantidade:
        valor_inicial = produto.estoque
        produto.estoque -= quantidade
        produto.save()

        # Registra a venda no histórico
        HistoricoEstoque.objects.create(
            produto=produto,
            tipo='venda',
            quantidade=quantidade,
            valor_inicial_estoque=valor_inicial,
            valor_final_estoque=produto.estoque,
            nome_cliente=nome_cliente,
            cpf_cliente=cpf_cliente,
            cnpj_cliente=cnpj_cliente,
            registro_venda=registro_venda
        )

        return JsonResponse({'status': 'success', 'message': 'Venda registrada com sucesso!', 'estoque': produto.estoque})
    else:
        return JsonResponse({'status': 'error', 'message': 'Quantidade inválida ou estoque insuficiente!'}, status=400)
    
@csrf_exempt
def ajustar_estoque(request, nome):
    produto = get_object_or_404(Produto, nome=nome)
    quantidade = int(request.POST.get('quantidade', 0))

    if quantidade != 0:
        valor_inicial = produto.estoque
        produto.estoque += quantidade
        produto.save()

        # Registra o ajuste no histórico
        HistoricoEstoque.objects.create(
            produto=produto,
            tipo='ajuste',
            quantidade=quantidade,
            valor_inicial_estoque=valor_inicial,
            valor_final_estoque=produto.estoque
        )

        return JsonResponse({'status': 'success', 'message': 'Estoque ajustado com sucesso!', 'estoque': produto.estoque})
    else:
        return JsonResponse({'status': 'error', 'message': 'Quantidade inválida!'}, status=400)

@csrf_exempt
def alterar_preco(request, nome):
    produto = get_object_or_404(Produto, nome=nome)
    novo_preco = request.POST.get('novo_preco')  # Recebe o novo preço do formulário

    if novo_preco:
        try:
            # Converte o novo preço para Decimal
            novo_preco = Decimal(novo_preco)
            if novo_preco <= 0:
                return JsonResponse({'status': 'error', 'message': 'O preço deve ser maior que zero!'}, status=400)

            preco_anterior = produto.preco
            produto.preco = novo_preco
            produto.save()

            # Registra a alteração de preço no histórico
            HistoricoEstoque.objects.create(
                produto=produto,
                tipo='alteracao_preco',
                quantidade=0,
                preco_anterior=preco_anterior,
                preco_novo=novo_preco,
                valor_inicial_estoque=produto.estoque,
                valor_final_estoque=produto.estoque
            )

            return JsonResponse({'status': 'success', 'message': 'Preço atualizado com sucesso!'})
        except (ValueError, TypeError):
            return JsonResponse({'status': 'error', 'message': 'Novo preço inválido!'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Novo preço inválido!'}, status=400)

def ver_historico(request, nome):
    produto = get_object_or_404(Produto, nome=nome)
    historico = HistoricoEstoque.objects.filter(produto=produto).order_by('-data_movimentacao')
    return render(request, 'produto/historico.html', {'produto': produto, 'historico': historico})