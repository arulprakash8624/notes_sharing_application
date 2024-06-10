from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('home.html', views.home, name='home'),
    path('register.html', views.register, name='register'),
    path('login.html', views.login, name='login'),  # Uncommented login_view
    path('result.html', views.submit_registration, name='result'),
    path('auth', views.login_view, name='login_view'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('upload',views.upload,name='upload'),
    path('delete',views.delete,name='delete')
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
