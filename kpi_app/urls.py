from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.index, name="index"),
    path("circles/", views.choose_circle, name="choose_circle"),
    path('circles/<int:cid>/', views.choose_kpi, name='choose_kpi'),
    path('circles/<int:cid>/<int:kid>/', views.update_kpi, name='update_kpi'),
    path("circles/<int:cid>/<int:kid>/saved/", views.saved, name="saved")
]

