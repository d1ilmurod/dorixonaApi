from django.urls import path
from .views import (
    KindApiView,
    ProductApiView,
    ProductCreateApiView,
    KindCreateApiView,
    ProductRetrieveUpdateDestroyAPIView,
    KindRetrieveUpdateDestroyAPIView

)

urlpatterns = [
    path('product/',ProductApiView.as_view()),
    path('product/create/',ProductCreateApiView.as_view()),
    path('product/<int:pk>/',ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('kind/',KindApiView.as_view()),
    path('kind/create/',KindCreateApiView.as_view()),
    path('kind/<int:pk>/',KindRetrieveUpdateDestroyAPIView.as_view()),
]