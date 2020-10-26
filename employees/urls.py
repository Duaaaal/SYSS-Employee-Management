from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employees import views
from employees.views import EmployeeViewSet, UserViewSet, api_root

router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


employee_list = EmployeeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
employee_detail = EmployeeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
