from django.conf.urls import url
from .views import index, professor_view

urlpatterns = [
    url(r'^$', index.mostrar, name='index'),
    url(r'^list$', professor_view.listar_professor, name='listar_professor'),
    #url(r'^new$', professor_view.criar_professor, name='criar_professor'),
    url(r'^edit/(?P<pk>\d+)$', professor_view.atualizar_professor, name='atualizar_professor'),
    url(r'^delete/(?P<pk>\d+)$', professor_view.excluir_professor, name='excluir_professor'),
]
