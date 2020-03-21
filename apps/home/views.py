from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Sections
from apps.blog.models import Post


# Create your views here.
def home(request):
    return render (request, 'home/index.html', {})


class IndexView(generic.TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = Sections.objects.filter(section='home').filter(active=1).order_by('ordered')

        # cargamos información para cada página exceptuando home
        for reg in context['pages']:
            if reg.link == 'blog':
                context[reg.link] = Post.objects.filter(publish_on__isnull=False).order_by('-publish_on')[:3]
            else:
                context[reg.link] = Sections.objects.filter(section=reg.link).filter(active=1).order_by('ordered')

        return context
