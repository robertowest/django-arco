from django.views.generic import TemplateView, ListView

from .models import Recurso

# Create your views here.
class RecursoTemplateView(TemplateView):
    # si no existe página index llamamos a otra función
    def get(self, request, *args, **kwargs):
        return RecursoListView.as_view()(request)


class RecursoListView(ListView):
    model = Recurso
    template_name = 'recurso/recurso_list.html'.format(app=__package__.split('.')[1])
    paginate_by = 15
