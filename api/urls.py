from django.urls import include, path
from api import views
from rest_framework import routers 
from api.views import delete_emp

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('home/', views.index_view, name='index'),
    path('delete_emp/<int:id>/',delete_emp,name ='delete_emp'),
]
       