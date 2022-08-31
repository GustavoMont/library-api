from django.contrib import admin
from django.urls import path, include
from book.urls import router as book_router
from users.urls import router as user_router
from loans.urls import router as loan_router
from users.views import CreateUserView, MyTokenObtainPairView
from rest_framework_simplejwt.views import (TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls, name='Admin'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/register/', CreateUserView.as_view(), name="register"),
    path('', include(loan_router.urls), name='loans'),
    path('', include(user_router.urls), name='users'),
    path('', include(book_router.urls), name='books'),
]
