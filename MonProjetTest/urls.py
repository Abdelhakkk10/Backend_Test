"""
URL configuration for MonProjetTest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import SignUpView, SignInView, AdminTaskListView, AdminTaskDetailView, UserTaskListView, UserTaskDetailView, CreateUserTaskView

from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="MonProjetTest API",
        default_version='v1',
        description="Documentation de l'API MonProjetTest",
        terms_of_service="https://www.MonProjetTest.com/terms/",
        contact=openapi.Contact(email="moussauiabdelhak@gmail.com"),
        license=openapi.License(name="Moussaoui Abdelhak "),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
  
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

   
    path('admin/', admin.site.urls),
    path('api/sign-up/', SignUpView.as_view(), name='sign-up'),
    path('api/sign-in/', SignInView.as_view(), name='sign-in'),
    path('api/admin/tasks/', AdminTaskListView.as_view(), name='admin-task-list'),
    path('api/admin/tasks/<int:pk>/', AdminTaskDetailView.as_view(), name='admin-task-detail'),
    path('api/user/tasks/', UserTaskListView.as_view(), name='user-task-list'),
    path('api/user/tasks/<int:pk>/', UserTaskDetailView.as_view(), name='user-task-detail'),
    path('api/user/create-task/', CreateUserTaskView.as_view(), name='create-user-task'),
    path('api/token/', obtain_auth_token, name='get-auth-token'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
