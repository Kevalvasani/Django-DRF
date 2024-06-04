from django.urls import path
from . import views


urlpatterns = [
    # Function Based API's
    path('stuinfo/<int:pk>', views.student_detail),
    path('stulist/', views.student_list),
    path('stucreate/', views.student_create),
    path('stuapifun/', views.student_fun_api),
    path('stuapiclass/', views.StudentAPI.as_view()),
    path('stuapiclassmodel/', views.StudentAPIModel.as_view()),
]