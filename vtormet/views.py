from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Letter, Cvetmet, Raddet, Recycling, Raddet_category
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.db.models import Q


def post_list(request):
    cvetmet = Cvetmet.objects.all()
    raddet_category = Raddet_category.objects.all()
    raddet = Raddet.objects.all()
    return render(request,'vtormetresurs/index.html',
                        {'cvetmet': cvetmet, 
                        'raddet_category' : raddet_category,
                        'raddet': raddet,}
                        )

def raddet_list(request, raddet_category_slug = None):
    raddet_category = Raddet_category.objects.get(slug=raddet_category_slug)
    raddet = Raddet.objects.filter(category=raddet_category.id)
    return render(request,'vtormetresurs/raddet.html', {
                                                        'raddet': raddet,
                                                        'raddet_category':raddet_category,
                                                        }
                  )

class create_letter(View):
    def post(self, request):
        letter = Letter()
        letter.phone = request.POST.get("phone")
        letter.category = 1
        letter.save()
        return HttpResponseRedirect("/")

    raise_exception = True


class delete_letter(LoginRequiredMixin, View):

    def get(self, request, id):
        try:
            letter = Letter.objects.get(id=id)
            letter.delete()
            return HttpResponseRedirect("/")
        
        except Post.DoesNotExist:
            return HttpResponseNotFound("<h2>letter not found</h2>")

    raise_exception = True


def recycling(request):

    search_query = request.GET.get('search', '')

    if search_query:
        recycling = Recycling.objects.filter(Q(FkkoCode__icontains=search_query) | Q(FkkoDescription__icontains=search_query))
    else:
        recycling = Recycling.objects.filter(Q(collection__icontains=1) | Q(transportation__icontains=1) | Q(processing__icontains=1) |  Q(disposal__icontains=1) | Q(utilization__icontains=1) | Q(placement__icontains=1))
    #FkkoCode;FkkoDescription;collection;transportation;processing;disposal;utilization;placement
    paginator = Paginator(recycling, 10)


    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    return render(request,'vtormetresurs/recycling/recycling.html', context=context)


def robots(request):
    return render(request, 'robots.txt')

def sitemap(request):
    return render(request, 'sitemap.xml')
