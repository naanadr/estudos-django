from django import forms
from django.core.mail import send_mail
from django.conf import settings


class ContactCourse(forms.Form):

    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    mensagem = forms.CharField(
        label='Mensagem/Dúvida', widget=forms.Textarea
    )

    def send_mail(self, course):
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'mensagem': self.cleaned_data['mensagem'],
        }
        subject = 'Contato sobre o Curso {}'.format(course)
        message = 'Nome: {name}; E-mail: {email}, {mensagem}'.format(**context)

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,
                  [settings.CONTACT_EMAIL])
