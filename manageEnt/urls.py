from re import template
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
import entreprise.views as vw

urlpatterns = [
    path("add-ent/", vw.add_entreprise, name='add-ent'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name="entreprise/index.html"), name='index')
]
