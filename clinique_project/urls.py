from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    # Page publique d'accueil (site vitrine Clinique Esprit)
    path("", TemplateView.as_view(template_name="public_home.html"), name="home"),

    # Admin Django (interface de gestion, protégée par login)
    path("admin/", admin.site.urls),

    # Tes autres apps
    path("patients/", include("patients.urls")),
    path("appointments/", include("appointments.urls")),
    path("billing/", include("billing.urls")),
]

# Servir les fichiers média en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
