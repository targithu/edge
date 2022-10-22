from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,CustomLoginView,RegisterPage, describe, foundational
from .views import feedback_form,pomodoro,first,foundational,acad_index,non_acad,outdoor,indoor,secondary,leisure,imag,alert,preparatory,middle,others
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('task-create/',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name='task-delete'),
    path('feedback/',feedback_form,name="feedback"),
    path('pomodoro/',pomodoro,name="pomodoro"),
    path('first/',first,name='first'),
    path('acad_index/',acad_index,name='acad_index'),
    path('foundational/',foundational,name='foundational'),
    path('secondary/',secondary,name='secondary'),
    path('preparatory/',preparatory,name='preparatory'),
    path('middle/',middle,name='middle'),
    path('outdoor/',outdoor,name='outdoor'),
    path('indoor/',indoor,name='indoor'),
    path('others/',others,name='others'),
    path('non_acad/',non_acad,name='non_acad'),
    path('imag/',imag,name="imag"),
    path('alert/',alert,name="alert"),
     path('describe/',describe,name="describe"),
     path('leisure/',leisure,name="leisure"),
]
#username:thisit
#password:urpasswor
