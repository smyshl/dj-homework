from django.urls import path

from measurement.views import SensorList, SensorView, SensorAdd, SensorUpdate, MeasurementAdd, MeasurementList, \
    SensorDetails

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensor/all', SensorList.as_view()),
    path('sensor/find/<pk>', SensorView.as_view()),
    path('sensor/add', SensorAdd.as_view()),
    path('sensor/update/<pk>', SensorUpdate.as_view()),
    path('temperature/add', MeasurementAdd.as_view()),
    path('temperature/all', MeasurementList.as_view()),
    path('sensor/details/<pk>', SensorDetails.as_view()),
]
