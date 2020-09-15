from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from mainpage.views import EndpointViewSet, MLAlgorithmViewSet, MLRequestViewSet, MLAlgorithmStatusViewSet

router = DefaultRouter(trailing_slash=False)
router.register("endpoints", EndpointViewSet, basename="endpoints")
router.register("mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register("mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register("mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    url('api/', include(router.urls)),
]