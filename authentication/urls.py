from django.urls import path
from authentication.views import auth_page, logout_user

app_name = 'authentication'

urlpatterns = [
    path('auth_page/', auth_page, name='auth_page'),
    path('logout/', logout_user, name='logout'),
]
