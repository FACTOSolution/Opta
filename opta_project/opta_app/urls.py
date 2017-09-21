from django.conf.urls import url, include
from .views import index, professor_view, grupo_view, projeto_view

projeto_patterns = [
    url(r'^projeto/new$', projeto_view.criar_projeto, name='criar_projeto'),
    url(r'^projeto/(?P<pk_proj>\d+)/', include([
        url(r'^detail/$', projeto_view.mostrar_projeto, name='mostrar_projeto'),
        url(r'^edit/$', projeto_view.atualizar_projeto, name='atualizar_projeto'),
        url(r'^delete/$', projeto_view.excluir_projeto, name='excluir_projeto'),
    ])),

]

grupo_patterns = [
    url(r'^grupo/new$', grupo_view.criar_grupo, name='criar_grupo'),
    url(r'^grupo/(?P<pk_grupo>\d+)/', include([
        url(r'^detail/$', grupo_view.mostrar_grupo, name='mostrar_grupo'),
        url(r'^edit/$', grupo_view.atualizar_grupo, name='atualizar_grupo'),
        url(r'^delete/$', grupo_view.excluir_grupo, name='excluir_grupo'),
    ])),
    url(r'^grupo/(?P<pk_grupo>\d+)/', include(projeto_patterns)),

]

urlpatterns = [
    url(r'^$', index.mostrar, name='index'),

    url(r'^professor/', include('django.contrib.auth.urls')),

    # urls from professor_view
    url(r'^professor/detail/$', professor_view.mostrar_professor, name='mostrar_professor'),
    url(r'^professor/(?P<pk_prof>\d+)/', include([
        url(r'^edit/$', professor_view.atualizar_professor, name='atualizar_professor'),
        url(r'^delete/$', professor_view.excluir_professor, name='excluir_professor'),
    ])),
    url(r'^professor/(?P<pk_prof>\d+)/', include(grupo_patterns)),

    url(r'^professor/list$', professor_view.listar_professor, name='listar_professor'),

    # urls from grupo_view
    url(r'^grupo/list$', grupo_view.listar_grupo, name='listar_grupo'),

    # urls from projeto_view
    url(r'^projeto/list$', projeto_view.listar_projeto, name='listar_projeto'),
]
