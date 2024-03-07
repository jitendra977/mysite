from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




from .views import *
from vegapp.views import *

urlpatterns = [

   path('',index,name="index_page"),
   path('vegapp/',index,name ='index_page'),
   path('add_recipe/', add_recipe, name='add_recipe'),
   path('delete_recipe/<int:id>/',delete_recipe,name ='delete_recipe'),
   path('edit_recipe/<int:id>/', edit_recipe, name='edit_recipe'),
   path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
