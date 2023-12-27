from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register("Category", CategoryView)
router.register("SubCategory", SubCategoryView)
router.register("Product", ProductView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/auth/", include("rest_framework.urls")),




    path("api/", include(router.urls)) 
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)