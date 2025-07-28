# Importa a função HttpResponse do Django
# Essa função serve para enviar uma resposta para o navegador (pode ser texto ou HTML)
from django.http import HttpResponse


# ==========================
# 📌 FUNÇÃO DA PÁGINA INICIAL
# ==========================
def home(request):
    # Retorna um conteúdo em HTML (não é só texto simples)
    # Entre as aspas """ """ podemos escrever código HTML
    # Aqui criamos um título <h1>, um parágrafo <p> e uma lista <ul> com links <a>
    return HttpResponse("""
        <h1>Bem-vindo ao Sistema de Convênios</h1>
        <p>Clique em um convênio para ver os requisitos de internação:</p>
        <ul>
            <!-- Cada <li> é um item da lista -->
            <!-- Cada <a href="..."> cria um link clicável -->
            <li><a href="/ameron/">Convênio Ameron</a></li>
            <li><a href="/bradesco/">Convênio Bradesco</a></li>
        </ul>
    """)


# ==========================
# 📌 FUNÇÃO DA PÁGINA AMERON
# ==========================
def ameron(request):
    # Retorna um conteúdo HTML com as informações do convênio Ameron
    # <h1> é um título grande, <p> é um parágrafo, <ul> é uma lista
    return HttpResponse("""
        <h1>Convênio Ameron</h1>
        <p><strong>Requisitos para internação:</strong></p>
        <ul>
            <li>Autorização (com data de senha dentro de validade)</li>
            <li>Documento com foto</li>
            <li>Carteirinha do convênio</li>
            <li>Pedido médico (original em mãos)</li>
        </ul>
    """)


# ============================
# 📌 FUNÇÃO DA PÁGINA BRADESCO
# ============================
def bradesco(request):
    # Retorna um conteúdo HTML com as informações do convênio Bradesco
    return HttpResponse("""
        <h1>Convênio Bradesco</h1>
        <p><strong>Requisitos para internação:</strong></p>
        <ul>
            <li>Documento com foto</li>
            <li>Carteirinha do convênio</li>
            <li>Guia de autorização</li>
        </ul>
    """)
