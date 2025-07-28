# Importa a função path, usada para criar rotas (endereços) no Django.
# Cada rota é um "endereço" que o usuário pode acessar no navegador.
from django.urls import path

# Importa o arquivo views.py desta mesma pasta.
# Isso é necessário porque as funções que mostram as páginas estão no views.py.
from . import views


# urlpatterns é uma lista onde registramos TODAS as rotas (URLs) deste app.
urlpatterns = [
    # Quando alguém acessar "http://127.0.0.1:8000/", o Django vai chamar a função home() do views.py
    path('', views.home),

    # Quando alguém acessar "http://127.0.0.1:8000/ameron/", o Django vai chamar a função ameron() do views.py
    path('ameron/', views.ameron),

    # Quando alguém acessar "http://127.0.0.1:8000/bradesco/", o Django vai chamar a função bradesco() do views.py
    path('bradesco/', views.bradesco),
]
