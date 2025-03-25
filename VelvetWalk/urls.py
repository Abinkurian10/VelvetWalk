from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from VelvetWalk_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('VelvetWalk_app.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='VelvetWalk_app/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 