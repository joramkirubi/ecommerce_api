from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from rest_framework.authtoken.views import obtain_auth_token
from .auth_views import RegisterView, LogoutView

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', obtain_auth_token, name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]

