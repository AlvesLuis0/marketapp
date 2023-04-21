from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("client/post", views.clientPost, name="clientPost"),
  path("product/post", views.productPost, name="productPost")
]