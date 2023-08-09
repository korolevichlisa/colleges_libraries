
from django import views
from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home),
    path("", include("testdb.urls")),
    # path('tfk/', views.tfk, name="tfk"),
    # path('mt/', views.mt, name="mt"),
    # path('nti/', views.nti, name="nti"),
    # path('kpa/', views.kpa, name="kpa"),

    #  path('show', views.display_images),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # New

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('fileLoad/', include('fileLoad.urls')),
#     path('', include('mainApp.urls')),
# ]