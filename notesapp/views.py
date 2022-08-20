from django.shortcuts import render,redirect
from django.views.generic import View, CreateView, FormView, TemplateView
from notesapp.forms import NotesForm
from notesapp.models import NotesModel
from django.urls import reverse_lazy

class CreateNoteView(CreateView):
    template_name = 'add_note.html'
    form_class = NotesForm
    model = NotesModel
    success_url = reverse_lazy('view_note')

class DisplayNoteView(View):
    def get(self, request, *args, **kwargs):
        qs=NotesModel.objects.all()
        return render(request, 'view_note.html', {'notes':qs})

class NoteDetailView(View):
    def get(self, request, *args, **kwargs):
        qs = NotesModel.objects.get(title=kwargs.get('title'))
        return render(request, 'detail_note.html', {'note': qs})

class NoteEditView(View):
    def get(self, request, *args, **kwargs):
        qs=NotesModel.objects.get(title=kwargs.get('title'))
        form=NotesForm(instance=qs)
        return render(request, 'edit_note.html', {'form':form})

    def post(self, request, *args, **kwargs):
        qs=NotesModel.objects.get(title=kwargs.get('title'))
        form=NotesForm(request.POST, instance=qs, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_note')
        else:
            return render(request, 'edit_note.html', {'form':form})

def notedelete(request, *args, **kwargs):
    note=NotesModel.objects.get(title=kwargs.get('title'))
    note.delete()
    return redirect('view_note')