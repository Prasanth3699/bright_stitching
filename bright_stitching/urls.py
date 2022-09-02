"""bright_stitching URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from main import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact_form', views.contact_form, name='contact_form'),
    path('contact', views.contact, name='contact'),

    # SAFETY WEAR
    path('safety_wear_page', views.safetywearpage, name='safety_wear_page'),
    path('safety_dress_upload', views.safety_dress_upload, name='safety_dress_upload'),
    path('safety_dress_detail<int:id>', views.safety_dress_details, name='safety_dress_detail'),
    path('safety_wear_delete/<id>', views.safety_wear_delete, name='safety_wear_delete'),



    # T-SHIRT
    path('tshirtpage', views.tshirtpage, name='tshirtpage'),
    path('t_shirt_upload',views.t_shirt_upload, name='t_shirt_upload'),
    path('t_shirt_details<int:id>', views.t_shirt_details, name='t_shirt_details'),
    path('t_shirt_delete/<id>', views.t_shirt_delete, name='t_shirt_delete'),

    # UNIFORMS
    path('uniformpage', views.uniformpage, name='uniformpage'),
    path('uniforms_upload',views.uniforms_upload, name='uniforms_upload'),
    path('uniform_details<int:id>', views.uniform_details, name='uniform_details'),
    path('uniform_delete/<id>', views.uniform_delete, name='uniform_delete'),

    # CAPS FLAGS
    path('cappage', views.cappage, name='cappage'),
    path('caps_details<int:id>', views.caps_details, name='caps_details'),
    path('cap_upload',views.cap_upload, name='cap_upload'),
    path('caps_delete/<id>', views.caps_delete, name='caps_delete'),
]
# path('edit_student/<str:student_id>', HodViews.edit_student,name="edit_student"),
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)