from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views import generic

from . import models

# Create your views here.
def home(request):
    return render (request, 'homepage/index.html', {})

def original(request):
    return render (request, 'homepage/original.html', {})


# class IndexView(generic.TemplateView):
#     template_name = 'homepage/index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['pages'] = models.Sections.objects.filter(section='home').filter(active=1).order_by('ordered')

    #     for reg in context['pages']:
    #         if reg.text_short:
    #             _section = reg.text_short[1:]

    #             if _section != 'home':
    #                 context[_section] = models.Sections.objects.filter(section=_section).filter(active=1).order_by('ordered')

    #     return context

    # def post(self, request, *args, **kwargs):
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     subject = request.POST.get('subject')
    #     message = request.POST.get('message')

    #     body = render_to_string(
    #         'email_content.html',
    #         {
    #             'name': name,
    #             'email': email,
    #             'subject': subject,
    #             'message': '<br />'.join(message.splitlines()),   # reemplazamos los saltos de línea por html
    #         },
    #     )
    #     send_mail = EmailMessage(
    #         subject = subject,
    #         body = body,
    #         from_email = email,
    #         to = ['roberto.west@gmail.com']
    #     )
    #     send_mail.content_subtype = 'html'
    #     try:
    #         send_mail.send()
    #     except BadHeaderError:
    #         return HttpResponse('Invalid header found.')
    #     return HttpResponseRedirect(reverse('homepage:home'))
