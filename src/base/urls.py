"""
URL configuration for base_de_datos_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from base.views import (
    PrestamoNestedView,
    PrestamoNestedOptimizedView,
    PrestamoFlatView,
    PrestamoNestedPaginatedView,
    PrestamoNestedOptimizedPaginatedView,
    PrestamoFlatPaginatedView,
)
urlpatterns = [
    path("prestamos/nested/", PrestamoNestedView.as_view()),
    path("prestamos/nested-optimized/", PrestamoNestedOptimizedView.as_view()),
    path("prestamos/flat/", PrestamoFlatView.as_view()),
    path("prestamos/nested-paginated/", PrestamoNestedPaginatedView.as_view()),
    path("prestamos/nested-optimized-paginated/", PrestamoNestedOptimizedPaginatedView.as_view()),
    path("prestamos/flat-paginated/", PrestamoFlatPaginatedView.as_view()),
]
