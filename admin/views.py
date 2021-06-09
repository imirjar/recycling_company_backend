from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import View
from vtormet.models import Letter, Cvetmet, Raddet, Recycling


from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class dash(LoginRequiredMixin, View):
	login_url = '/admin/'
	
	def get(self, request):
		letter = Letter.objects.all()
		try:
			return render(request,'vtormetresurs/admin/index.html', {'letter': letter})
		except DoesNotExist:
			return HttpResponseRedirect("/admin")