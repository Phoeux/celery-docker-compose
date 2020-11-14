from django.urls import path
from book.views import hello, check


urlpatterns = [
	path("", hello),
	path('check/', check),
]