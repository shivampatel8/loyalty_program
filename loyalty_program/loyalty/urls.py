from rest_framework import routers
from loyalty import views
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'person', views.PersonViewSet)

from . import views

urlpatterns = [
    path('', include(router.urls)),
    path('index', views.index, name='index'),
    # path('hello/', views.HelloView, name='hello'),
    # path('hello1/', views.HelloView1.as_view(), name='hello'),

    path('api-auth/',views.ExampleView.as_view(), name='index'),
    path('login/',views.person_detail),
    path('getPoints/',views.GetPoints.as_view(),name="getPoints"),
    path('allPoints/',views.AllPoints.as_view(),name="allPoints"),
    path('addPoints/',views.AddPoints.as_view(),name="addPoints")
    
]