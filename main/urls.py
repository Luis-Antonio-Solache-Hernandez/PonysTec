from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^mijson$', views.json, name="json"),
    url(r'^reporte$', views.reporte, name="reporte"),
    url(r'^pagina2$', views.pagina2, name="pag2"),
    url(r'^productos$', views.Productos, name="productos"),
    url(r'^alta/producto$', views.creaProducto, name="creaProducto"),
    url(r'^editar/producto/(?P<pk>\d+)$', views.editarProducto, name="editarProducto"),
    # urls para logout y login
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}),
    url(r'^accounts/login/$', auth_views.login, {
        'template_name': 'login.html'
    }),
]
