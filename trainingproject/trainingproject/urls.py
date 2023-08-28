from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("helloworld/", include("helloworld.urls")),  # Include your app's URLs here\
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("doc/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("doc/redoc/",SpectacularRedocView.as_view(url_name="schema"),name="redoc",),
]
