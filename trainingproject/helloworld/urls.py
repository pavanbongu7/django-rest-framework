from django.urls import path

from .views import HelloWorldView

urlpatterns = [
    path("api", HelloWorldView.as_view(), name="hello-world"),
]
