from django.urls import path
from .views import blog_app

urlpatterns = [
    path('blog2/', blog_app)
]