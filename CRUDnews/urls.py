from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from News import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.NewsPage, name='news'),
    path('addnews/', views.addNews, name='AddNews'),
    path('register/', views.registration, name='register'),
    path('login/', views.user_login, name='login'),
    path('logOut/', auth_views.LogoutView.as_view(next_page='login'), name='logout')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
