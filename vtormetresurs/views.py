from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .forms import LoginForm

from django.contrib.auth.mixins import LoginRequiredMixin

class Signin(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')



