from django.urls import path
from . import views

urlpatterns = [
    # path("getapi/", views.get_api),
    # path("postapi/", views.post_api),
    path("studentapi/", views.student_api),
    path("studentapi/<int:pk>", views.student_apiview),
    path("studentapiclass/<int:pk>", views.StudentClassAPIview.as_view()),
    path("studentapiclass/", views.StudentClassAPIview.as_view()),
    path("studentlist/", views.Studentlist.as_view()),
    path("studentcreate/", views.Studentcreate.as_view()),
    path("studentretrieve/<int:pk>", views.Studentretrieve.as_view()),
    path("studentupdate/<int:pk>", views.Studentupdate.as_view()),
    path("studentdestroy/<int:pk>", views.Studentdestroy.as_view()),
    path("student_l_c/", views.Student_l_c.as_view()),
    path("student_r_u_d/<int:pk>", views.Student_r_u_d.as_view()),
    path("student_c_l/", views.Student_c_l.as_view()),
    path("student_c_c/", views.Student_c_c.as_view()),
    path("student_c_r/<int:pk>", views.Student_c_r.as_view()),
    path("student_c_u/<int:pk>", views.Student_c_u.as_view()),
    path("student_c_d/<int:pk>", views.Student_c_d.as_view()),
    path("student_c_l_c/", views.Student_c_l_c.as_view()),
    path("student_c_r_u_d/<int:pk>", views.Student_c_r_u_d.as_view()),

]
