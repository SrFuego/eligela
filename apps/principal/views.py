from django.views.generic.base import TemplateView

from .models import Beneficio, Carrera, Colaborador


class IndexView(TemplateView):
    template_name = 'principal/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['beneficios'] = Beneficio.objects.all()
        context['colaboradores'] = Colaborador.objects.all()
        return context


class ConferenciaView(TemplateView):
    template_name = 'principal/conferencia.html'

    def get_context_data(self, **kwargs):
        context = super(ConferenciaView, self).get_context_data(**kwargs)
        context['carreras'] = Carrera.objects.all()
        return context
