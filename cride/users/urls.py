
#Django
from django.urls import path, include
#DRF
from rest_framework.routers import DefaultRouter

from .views import users as user_views

router = DefaultRouter()
router.register(r"users", user_views.UserViewSet, basename = "users")

urlpatterns= [
  path("", include(router.urls))
]

# urlpatterns= [
#   path("users/login", UserLoginAPIView.as_view(), name = "login"),
#   path("users/signup", UserSignUpAPIView.as_view(), name = "signup"),
#   path("users/verify", AccountVerificationAPIView.as_view(), name = "verify"),
# ]
