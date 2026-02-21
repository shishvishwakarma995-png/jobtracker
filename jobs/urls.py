from django.urls import path
from . import views

urlpatterns = [
    path('',          views.DashboardView.as_view(), name='dashboard'),
    path('jobs/',     views.JobListView.as_view(),   name='job-list'),
    path('jobs/add/', views.JobCreateView.as_view(), name='job-create'),
    path('jobs/<int:pk>/edit/',   views.JobUpdateView.as_view(), name='job-update'),
    path('jobs/<int:pk>/delete/', views.JobDeleteView.as_view(), name='job-delete'),
    path('register/', views.RegisterView.as_view(), name='register'),  # ← new
]