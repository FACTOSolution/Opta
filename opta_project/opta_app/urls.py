from django.conf.urls import url, include
from .views import index, professor_view, grupo_view, projeto_view

urlpatterns = [
    url(r'^$', index.mostrar, name='index'),

    url(r'^professor/', include('django.contrib.auth.urls')),

    # urls from professor_view
    url(r'^professor/detail', professor_view.mostrar_professor, name='mostrar_professor'),
    url(r'^professor/list$', professor_view.listar_professor, name='listar_professor'),
    #url(r'^professor/new$', professor_view.criar_professor, name='criar_professor'),
    url(r'^professor/edit/(?P<pk>\d+)$', professor_view.atualizar_professor, name='atualizar_professor'),
    url(r'^professor/delete/(?P<pk>\d+)$', professor_view.excluir_professor, name='excluir_professor'),

    # urls from grupo_view
    url(r'^grupo/list$', grupo_view.listar_grupo, name='listar_grupo'),
    url(r'^professor/grupo/new$', grupo_view.criar_grupo, name='criar_grupo'),
    url(r'^professor/grupo/edit/(?P<pk>\d+)$', grupo_view.atualizar_grupo, name='atualizar_grupo'),
    url(r'^professor/grupo/delete/(?P<pk>\d+)$', grupo_view.excluir_grupo, name='excluir_grupo'),

    # urls from projeto_view
    url(r'^projeto/list$', projeto_view.listar_projeto, name='listar_projeto'),
    url(r'^projeto/new$', projeto_view.criar_projeto, name='criar_projeto'),
    url(r'^projeto/edit/(?P<pk>\d+)$', projeto_view.atualizar_projeto, name='atualizar_projeto'),
    url(r'^projeto/delete/(?P<pk>\d+)$', projeto_view.excluir_projeto, name='excluir_projeto'),
]
