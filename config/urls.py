from django.contrib import admin
from django.urls import path, include
from book.urls import router as book_router
from users.urls import router as user_router
from loans.urls import router as loan_router
from users.views import CreateUserView, MyTokenObtainPairView
from rest_framework_simplejwt.views import (TokenRefreshView)

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view


schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Library API",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
)



urlpatterns = [
    path('admin/', admin.site.urls, name='Admin'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
    path('auth/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/register/', CreateUserView.as_view(), name="register"),
    path('', include(loan_router.urls), name='loans'),
    path('', include(user_router.urls), name='users'),
    path('', include(book_router.urls), name='books'),
]
