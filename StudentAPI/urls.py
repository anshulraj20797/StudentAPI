from django.urls import path,include
from .views import StudentView
from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'students/<int:id>',StudentView.as_view(), basename='Student')

urlpatterns = [
    # path('',include(router.urls)),
    path('students/',StudentView.as_view())
]