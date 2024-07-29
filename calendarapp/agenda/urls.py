from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'categorias', views.CategoriasViewSet)


urlpatterns = [
    path('categorias/', views.CategoriaCreateView.as_view()),
    path('categorias/cantidad/', views.categoria_count),
    path('Eventos/filtrar/unidades/', views.Eventos_en_unidades),
    path('Eventos/reporte/', views.reporte_Eventos),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
