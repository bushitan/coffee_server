
from django.conf.urls import url
from .views import  *

urlpatterns = [
    url(r'^index/',MapIndex.as_view()),
    url(r'^search/poi/',MapGetPOI.as_view()),
    url(r'^search/article/',MapGetArticle.as_view()),
]
