from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)

print(router.urls)

urlpatterns = [
    path('', include(router.urls))
]


# urlpatterns = [
#     path('products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
#     path('products/<slug:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update' ...}))
# ]