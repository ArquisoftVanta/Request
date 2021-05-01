from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from proyecto.views.request_view import RequestList
from proyecto.views.request_view import RequestDetail
from proyecto.views.request_view import RequestU
from proyecto.views.request_view import RequestActive
from proyecto.views.request_view import RequestService
from proyecto.views.coordenates_request_view import CoordinatesDetail
from proyecto.views.coordenates_request_view import CoordinatesList
from proyecto.views.coordenates_request_view import CoordinatesbyRequest
from proyecto.views.service_view import ServiceDetail
from proyecto.views.service_view import ServiceList
router = DefaultRouter()

urlpatterns = [

    path('request/', RequestList.as_view()),
    path('requestUser/', RequestU.as_view()),
    path('requestActive/', RequestActive.as_view()),
    path('requestService/', RequestService.as_view()),
    path('request/<int:pk>', RequestDetail.as_view()),
    path('coordinatesRequest/', CoordinatesbyRequest.as_view()),
    path('coordinates/', CoordinatesList.as_view()),
    path('coordinates/<int:pk>', CoordinatesDetail.as_view()),
    path('service/', ServiceList.as_view()),
    path('service/<int:pk>', ServiceDetail.as_view()),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)