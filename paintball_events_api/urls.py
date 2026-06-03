from django.contrib import admin
from django.urls import path

from paintball.api import api
from django.views.generic import RedirectView
from paintball.views import about_api, model_page, making_of

urlpatterns = [
    path("", RedirectView.as_view(url="/sobre-api/", permanent=False)),
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path("sobre-api/", about_api, name="about_api"),
    path("modelo/", model_page, name="model_page"),
    path("making-of/", making_of, name="making_of"),
]