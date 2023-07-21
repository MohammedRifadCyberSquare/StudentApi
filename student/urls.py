from . import views
from django.urls import path



urlpatterns = [
  
    path('Register',views.register_student, name='register_student'),
    path('List',views.students_list, name='students_list'),
    path('Detail/<int:id>',views.student_details, name='student_details'),
    path('Update/<int:id>',views.update_student, name='update_student'),
    path('Delete/<int:id>',views.delete_student, name='delete_student'),
]