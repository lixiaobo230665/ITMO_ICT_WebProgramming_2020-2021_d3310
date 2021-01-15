
from django.urls import path
from Students import views
urlpatterns = [
    path("dis_list/", views.discipline_list),
    path("hw_data/<int:id_dis>/", views.homeworke_data),
    path("hw_updata/<int:pk>/",views.hwUpdateView.as_view()),
    path("student/<int:pk>/",views.student_data.as_view()),
    path("student_list/",views.student_list.as_view()),
    path("p_list/<int:pk>/", views.pUpdateView.as_view()),
    path("set_hw/", views.create_hw.as_view()),
    path("add_hw/", views.add_hw.as_view()),
    path("del_hw/<int:pk>/", views.delete_hw),
    path("del_HW/<int:pk>/", views.delete_HW),
]