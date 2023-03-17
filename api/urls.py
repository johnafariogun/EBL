from django.urls import path
from .views import ContactCreateView,home, RegistrationCreateView, getfile
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="EBL API",
      default_version='v1.',
      description="Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="afariogun.john2002@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('contact', ContactCreateView.as_view(), name='contact'),
    path('register', RegistrationCreateView.as_view(), name='register'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("", home)
]
