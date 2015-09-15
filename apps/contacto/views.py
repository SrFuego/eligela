# Python imports


# Django imports
from django.views.generic import FormView


# Local imports
from .forms import ContactoForm


# Create your views here.
class ContactanosView(FormView):

    form_class = ContactoForm
    template_name = 'contacto/index.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(ContactanosView, self).form_valid(form)
