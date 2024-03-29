from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from employeemanagement.views import add_employee, delete_employee, emp_home, update_employee

from monthlybudget.views import add_transactions, budget_home




from .views import *
from vegapp.views import *

urlpatterns = [

   path('',index,name="index_page"),
   path('vegapp/',index,name ='index_page'),
   path('add_recipe/', add_recipe, name='add_recipe'),
   path('delete_recipe/<int:id>/',delete_recipe,name ='delete_recipe'),
   path('edit_recipe/<int:id>/', edit_recipe, name='edit_recipe'),

   #employee
   path('employeemanagement/',include('employeemanagement.urls')),
   
   # include budget url -
   path('monthlybudget/',include('monthlybudget.urls')),
   

   #include api path
   path('api/',include('api.urls')),
   
   
   path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
