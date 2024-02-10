from django.urls import path
from . import views

urlpatterns=[
    # path('',views.model_predict,name='model_predict'),
      path('upload/', views.upload_image, name='upload_image'),
]
