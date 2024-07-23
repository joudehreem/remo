from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ),
    path('add_courses',views.add_courses),
    path('coursers/<str:id>/destroy',views.review_course),
    path('coursers/destroy', views.remove_course),
    path('course/<str:id>/comment/',views.comment),
    path('add_comment/<str:id>',views.add_comment)
]

