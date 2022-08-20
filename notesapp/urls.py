from django.urls import path
from notesapp import views

urlpatterns = [
    path('add/', views.CreateNoteView.as_view(), name='add_note'),
    path('view/', views.DisplayNoteView.as_view(), name='view_note'),
    path('detail/<str:title>', views.NoteDetailView.as_view(), name='note_detail'),
    path('edit/<str:title>', views.NoteEditView.as_view(), name='note_edit'),
    path('delete/<str:title>', views.notedelete, name='note_delete')
]