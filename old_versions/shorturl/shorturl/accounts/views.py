from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.conf import settings

from .forms import RegisterForm


class RegisterPageView(CreateView):

    template_name = 'accounts/register.html'
    form_class = RegisterForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('home:index')
        else:
            return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def get_context_data(self, **kwargs):
        context = super(RegisterPageView, self).get_context_data(**kwargs)
        return context
