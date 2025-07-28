# Importa os módulos necessários do Django
from django.contrib import admin               # Permite acessar o painel de administração do Django
from django.urls import path, include         # "path" cria rotas; "include" permite usar rotas de outros arquivos

# urlpatterns é uma lista que guarda TODAS as rotas principais do projeto
urlpatterns = [
    # Rota padrão para acessar o painel de administração do Django
    # Quando digitamos "http://127.0.0.1:8000/admin/", abre o painel admin
    path('admin/', admin.site.urls),

    # Essa linha conecta o arquivo "urls.py" do app "convenios" ao projeto principal
    # Significa que TODAS as rotas definidas em convenios/urls.py serão usadas aqui
    # Quando alguém acessa "http://127.0.0.1:8000/", o Django olha as rotas do app convenios
    path('', include('convenios.urls')),
]
