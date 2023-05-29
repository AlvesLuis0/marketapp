from django.urls import path

from .controllers import productController
from .controllers import employeeController
from .controllers import authController

urlpatterns = [
  path("", productController.getProducts, name="index"),
  path("product/register/", productController.registerProduct, name="registerProduct"),
  path("employee/register/", employeeController.registerEmployee, name="registerEmployee"),
  path("login/", authController.loginController, name="login"),
  path("logout/", authController.logoutController, name="logout")
]