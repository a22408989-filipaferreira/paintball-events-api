from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from paintball.api import api as paintball_api
from paintball.views import about_api, model_page, making_of

from projetos.api import api as projetos_api
from restaurante.api import api as restaurante_api
from filmes.api import api as filmes_api

urlpatterns = [
    path("", RedirectView.as_view(url="/sobre-api/", permanent=False)),
    path("admin/", admin.site.urls),

    path("api/", paintball_api.urls),
    path("api/projetos/", projetos_api.urls),
    path("api/restaurante/", restaurante_api.urls),
    path("api/filmes/", filmes_api.urls),

    path("sobre-api/", about_api, name="about_api"),
    path("modelo/", model_page, name="model_page"),
    path("making-of/", making_of, name="making_of"),
]