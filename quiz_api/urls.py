from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Category', views.CategoryView)
router.register('Difficult', views.DifficultView)
router.register('Type', views.TypeView)
router.register('Question', views.QuestionView)

urlpatterns = [
    path('quiz/', include(router.urls))
]