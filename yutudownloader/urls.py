from django.urls import path, include
from . import views

app_name = "yutudownloader"

urlpatterns = [
    path('', views.index, name="home"),
    path('download/', views.download, name="download"),
    path('download/<resolution>/', views.yt_download_done, name="download_done")

]

