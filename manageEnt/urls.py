from django.contrib import admin
from django.urls import path
import entreprise.views as vw

urlpatterns = [
    path('', vw.index, name="home"),
    path('admin/', admin.site.urls),
]
