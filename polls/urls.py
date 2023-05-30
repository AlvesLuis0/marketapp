from django.urls import path

from .controllers import productController
from .controllers import employeeController
from .controllers import authController
from .controllers import cartController

urlpatterns = [
  path("", productController.getAllProducts, name="index"),
  path("product/register/", productController.registerProduct, name="registerProduct"),
  path("product/update/<int:pk>/", productController.updateProduct, name="updateProduct"),
  path("product/delete/<int:pk>/", productController.deleteProduct, name="deleteProduct"),
  path("product/<int:pk>/", productController.getProduct, name="getProduct"),
  path("product/add/<int:pk>/", cartController.addToCart, name="addToCart"),
  path("product/cart/", cartController.getCart, name="getCart"),
  path("product/cart/delete/<int:pk>/", cartController.deleteFromCart, name="deleteFromCart"),
  path("product/cart/checkout/", cartController.checkout, name="checkout"),

  path("employee/", employeeController.getAllEmployees, name="getAllEmployees"),
  path("employee/register/", employeeController.registerEmployee, name="registerEmployee"),
  path("employee/update/<int:pk>/", employeeController.updateEmployee, name="updateEmployee"),
  path("employee/delete/<int:pk>/", employeeController.deleteEmployee, name="deleteEmployee"),
  path("employee/<int:pk>/", employeeController.getEmployee, name="getEmployee"),

  path("login/", authController.loginController, name="login"),
  path("logout/", authController.logoutController, name="logout")
]