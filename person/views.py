from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View, DetailView, UpdateView, ListView, CreateView, TemplateView
from django.views.generic.base import RedirectView
from django.views.generic.detail import SingleObjectMixin
from django.utils.decorators import method_decorator


from person.models import Person, PersonVitals, PersonContacts, PersonDemographic, PersonGuardian

from person.forms import PersonForm

# Create your views here.
class LoginRequiredMixin(object):
    @method_decorator(login_required)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    
class IndexView(ListView):
    model = Person
    form_class = PersonForm
    template_name = 'person/index.html'
    context_object_name = 'person_list'
    
class PersonMixin(object):
    fields = ('first_name', 'surname', 'home_village', 'person_photo')

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PersonMixin, self).form_valid(form)

    
class PersonCreateView(PersonMixin, CreateView):
    model = Person    
    success_msg = 'Person successfully added!'
    success_url = '/patient/'
    template_name = 'person/create_person.html'
    
    
class PersonUpdateView(PersonMixin, UpdateView):    
    template_name = 'person/update_person.html'
    model = Person
    context_object_name = 'person'
    success_url = '/patient/'

    
class PersonDetailView(ListView):
    template_name = 'person/profile.html'

    def get(self, request, *args, **kwargs):
        self.object = get_object_or_404(Person, pk = kwargs['pk'])
        return super(PersonDetailView, self).get(request, *args, **kwargs)
    
    def get_queryset(self):
        return self.object

    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        context['person'] = self.object
        try:
            context['demographic'] = PersonDemographic.objects.get(person = self.object)
            context['vitals'] = PersonVitals.objects.get(person = self.object)
            context['contacts'] = PersonContacts.objects.get(person = self.object)
            context['nextofkin'] = PersonGuardian.objects.get(person = self.object)
        except:
            pass
        
        return context

    model = PersonVitals
