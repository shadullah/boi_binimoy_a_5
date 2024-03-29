from django.urls import path,include
from .views import UserRegistration,UserLoginView,user_logout, editProfile

urlpatterns = [
    path('register/', UserRegistration.as_view(), name = 'register'),
    path('login/', UserLoginView.as_view(), name = 'login'),
    path('logout/', user_logout, name = 'logout'),
    path('profile/', editProfile, name = 'profile')
]