from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views
from users.views import CustomLoginView  
from users.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("users.urls")),

    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
