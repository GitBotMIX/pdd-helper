from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='home'),
    path('pdd', views.pdd, name='pdd'),
    path('helper', views.helper, name='helper'),
    path('question/<int:num>', views.question_number),

]
