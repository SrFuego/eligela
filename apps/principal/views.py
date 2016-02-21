from django.views.generic.base import TemplateView
from django.views.generic import RedirectView

from .models import Beneficio, Carrera, Colaborador


class IndexView(TemplateView):
    template_name = 'principal/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['beneficios'] = Beneficio.objects.all()
        context['colaboradores'] = Colaborador.objects.all()
        return context


class EntrevistaView(TemplateView):
    template_name = 'principal/entrevista.html'

    def get_context_data(self, **kwargs):
        context = super(EntrevistaView, self).get_context_data(**kwargs)
        context['carreras'] = Carrera.objects.all()
        return context


class CarmenGitHubView(RedirectView):
    permanent = True
    url = 'http://carmenluyo.github.io/elige.la/'
