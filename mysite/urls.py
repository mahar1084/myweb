from django.contrib import admin
from django.urls import path, include
from mysite import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from mysite.views import (
    my_home, about, dashboard, not_found_artikel,
    UserProfileListAPIView, UserProfileRetrieveUpdateAPIView
)

# Import view login/logout/registrasi
from mysite.authentication import login, logout, registrasi

# Import artikel views
from artikel.views import detail_artikel, artikel_tidak_ditemukan, artikel_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_home, name="my_home"),
    path('artikel/<int:id>', detail_artikel, name="detail_artikel"),
    path('artikel-tidak-ditemukan/', artikel_tidak_ditemukan, name="artikel_tidak_ditemukan"),
    path('about', about, name="about"),
    path('dashboard/', dashboard, name="dashboard"),
    path('dashboard/artikel_list', artikel_list, name="artikel_list"),

    # Routing artikel dan dashboard
    path('dashboard/', include("artikel.urls")),
    path('api/', include("artikel.urls")),

    # ✅ Routing login, logout, registrasi (utama)
    path('auth/login/', login, name="auth-login"),
    path('auth/logout/', logout, name="logout"),
    path('auth/registrasi/', registrasi, name="auth-registrasi"),

    # ✅ Tambahan: URL alternatif agar tidak 404 jika URL lama tersebar
    path('auth-login', login),
    path('auth-logout', logout),
    path('auth-registrasi', registrasi),

    # API user profile
    path('api/users/', UserProfileListAPIView.as_view(), name='api_user_list'),
    path('api/users/<int:pk>/', UserProfileRetrieveUpdateAPIView.as_view(), name='api_user_detail'),
    path('api/me/', UserProfileRetrieveUpdateAPIView.as_view(), name='api_my_profile'),
]

# Untuk Media
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# CKEditor
urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
