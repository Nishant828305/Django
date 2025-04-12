
from django.urls import path 
from . import views
 #  localhost:8000/boom
  #  localhost:8000/boom/order
urlpatterns = [
    path('',views.all_chai , name ='all_home'), 
    path('<int:chai_id>/',views.chai_details, name ='chai_details'), 
    path('order/',views.order , name ='chai_order'), 
]