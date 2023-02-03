from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Complaints, Files
from .forms import ComplaintsForm


class ComplaintsListView(ListView):
    model = Complaints
    form_class = ComplaintsForm
    template_name = 'list.html'
    context_object_name = 'complaints'


class ComplaintsCreateView(CreateView):
    model = Complaints
    form_class = ComplaintsForm
    template_name = 'create.html'
    context_object_name = 'complaints'
    success_url = reverse_lazy('complaints_create')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('files')
        if form.is_valid():
            id = form.save().pk
            complaint = Complaints.objects.get(pk=id)
            if files:
                for f in files:
                    fl = Files(complaint=complaint, file=f)
                    fl.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)




