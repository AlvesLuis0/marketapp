from django.urls import path

from .controllers import productController
from .controllers import employeeController
from .controllers import authController

urlpatterns = [
  path("", productController.getAllProducts, name="index"),
  path("product/register/", productController.registerProduct, name="registerProduct"),
  path("product/update/<int:pk>/", productController.updateProduct, name="updateProduct"),
  path("product/delete/<int:pk>/", productController.deleteProduct, name="deleteProduct"),
  path("product/<int:pk>/", productController.getProduct, name="getProduct"),
  path("employee/register/", employeeController.registerEmployee, name="registerEmployee"),
  path("login/", authController.loginController, name="login"),
  path("logout/", authController.logoutController, name="logout")
]