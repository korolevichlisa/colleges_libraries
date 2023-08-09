# # from django import views
# # from django.contrib import admin
# # from django.urls import path
# # from . import views

# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('', views.home),
# #     path('tfk/', views.tfk, name="tfk"),
# #     path('mt/', views.mt, name="mt"),
# #     path('nti/', views.nti, name="nti"),
# #     path('kpa/', views.kpa, name="kpa"),
    

# # ]

from django import views
from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('tfk/', views.tfk, name="tfk"),
    path('mt/', views.mt, name="mt"),
    path('nti/', views.nti, name="nti"),
    path('kpa/', views.kpa, name="kpa"),
    # path("tfk/", tfk.as_view(), name="tfk"),
]