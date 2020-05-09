from django.contrib import admin
from django.urls import path
from webscraper.views import WebScrapingView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('corona/', WebScrapingView.as_view(), name='index')
]
