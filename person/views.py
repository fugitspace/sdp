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


# Create your views here.
class LoginRequiredMixin(object):
    @method_decorator(login_required)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    
class IndexView(TemplateView):
    template_name = 'person/index.html'
    
class PersonMixin(object):
    pass
    
class PersonCreateView(TemplateView):
    template_name = 'person/create_person.html'
    
    
class PersonUpdateView(TemplateView):    
    template_name = 'person/update_person.html'
