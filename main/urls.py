from django.urls import path
from . import views


urlpatterns = [
    path('store_list/', views.StoreList.as_view()),
    path('set_visit/', views.SetVisit.as_view())
]