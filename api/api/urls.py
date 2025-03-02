from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from recipes import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Recipe API",
        default_version='v1',
        description="API documentation for the Recipe App",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@recipe.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

router = routers.DefaultRouter()
router.register(r'recipes', views.RecipeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
