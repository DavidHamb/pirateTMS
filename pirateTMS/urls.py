from django.contrib import admin
from django.urls import path
from tms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('targets/', views.targets, name='targets'),
    path('target_detail/<int:id>/', views.target_detail, name='target-detail'),
    path('targets/add/', views.targets_add, name='targets-add'),
    path('target_detail/<int:id>/update/', views.target_update, name='target-update'),
    path('target_detail/<int:id>/delete/', views.target_delete, name='target-delete'),
    path('target_detail/<int:id>/add_note/', views.add_note, name='add-note'),
    path('delete_note/<int:id>/', views.delete_note, name='delete-note'),
    path('vulnerabilities/', views.vulnerabilities, name='vulnerabilities'),
    path('vulnerabilities/add/', views.vulnerabilities_add, name='vulnerabilities-add'),
    path('ressources/', views.ressources, name='ressources'),
    path('ressources/add/', views.ressources_add, name='ressources-add'),
    path('checklist/', views.checklist, name='checklist'),
]
