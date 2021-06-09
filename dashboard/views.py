from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.views.generic import View
from django.core.exceptions import ValidationError
from .forms import ActCreateForm, ChoosePerformerForm, CreateAnswerForm, CustomerInitiatorForm
from .models import Requisition, Answer, Performer, RequisitionAnswer
from .mail_templates import *
from .utils import file_size


login_url = '/login/'
acts = Requisition.objects.all()
performers = Performer.objects.all()

@login_required
def accept_req_answ(request, id):
    req_answ = RequisitionAnswer.objects.get(id=id)
    req_answ.accept(request)
    try:
        send_acception_mail(req_answ)
        return HttpResponseRedirect('/dashboard/act_list')
    except:
        HttpResponse('Ответ отправителя был подтвержден но почта с уведомлением не была отправлена!')


@login_required
def decline_req_answ(request, id):
    req_answ = RequisitionAnswer.objects.get(id=id)
    req_answ.decline(request)
    try:
        send_decline_mail(req_answ)
        return HttpResponseRedirect('/dashboard/act_list')
    except:
        HttpResponse('Ответ отправителя был отклонен но почта с уведомлением не была отправлена!')

class ActList(LoginRequiredMixin, View):

    def get(self, request):
        req_answ = RequisitionAnswer.objects.filter(accepted_date=None)
        form = ChoosePerformerForm()
        return render(request, 'dashboard/act_list.html', {
                'acts':req_answ,
                'performers':performers,
                'form':form
                                                           })

    def post(self, request):#'requisition', 'performer'
        form = ChoosePerformerForm(request.POST)
        if form.is_valid():
            requisition = form.cleaned_data['requisition']
            performer = form.cleaned_data['performer']
            req_answ = RequisitionAnswer.objects.get(requisition=requisition)
            req_answ.performer = performer
            req_answ.save()
            try:
                send_apointment_mail(req_answ)
                return HttpResponseRedirect('/dashboard/act_list')
            except:
                HttpResponse('Исполнитель был назначен но почта с уведомлением не была отправлена!')


class ActListArchive(LoginRequiredMixin, View):

    def get(self, request):
        req_answ = RequisitionAnswer.objects.all().exclude(accepted_date=None)
        form = ChoosePerformerForm()
        return render(request, 'dashboard/act_list.html', {
            'acts':req_answ,
                'performers':performers,
                'form':form
                                                           })


class ActCreate(LoginRequiredMixin, View):

    def get(self, request):
        requisition_form = ActCreateForm()
        customer_initiator_form = CustomerInitiatorForm()
        return render(request, 'dashboard/act_form.html', {
            'requisition_form' : requisition_form,
            'customer_initiator_form' : customer_initiator_form
            }
            )

#customer_initiator_form.cleaned_data['data']
    def post(self, request):
        requisition_form = ActCreateForm(request.POST, request.FILES)
        customer_initiator_form = CustomerInitiatorForm(request.POST)
        try:
            if requisition_form.is_valid():#не придумал как автоматическм прикрутить user к методу модели save()
                requisition = requisition_form.save()
                if  customer_initiator_form.is_valid():
                    requisition = Requisition.objects.get(id = requisition.id)
                    req_answ = RequisitionAnswer.objects.get(requisition = requisition)
                    req_answ.initiator_name = customer_initiator_form.cleaned_data['initiator_name']
                    req_answ.initiator_phone = customer_initiator_form.cleaned_data['initiator_phone']
                    req_answ.initiator_representative = customer_initiator_form.cleaned_data['initiator_representative']
                    req_answ.save()
                    return HttpResponseRedirect('/dashboard/act_create')
        except:
            HttpResponse('Что то пошло не так, проверьте не занят ли номер обращения!')


class ActEdit(LoginRequiredMixin, View):

    def get(self, request, requisition_answer_id):
        requisition_form = ActCreateForm()
        customer_initiator_form = CustomerInitiatorForm()
        return render(request, 'dashboard/act_edit.html', {
            'requisition_form' : requisition_form,
            'customer_initiator_form' : customer_initiator_form
            }
            )

#customer_initiator_form.cleaned_data['data']
    def post(self, request):
        requisition_form = ActCreateForm(request.POST, request.FILES)
        customer_initiator_form = CustomerInitiatorForm(request.POST)
        try:
            if requisition_form.is_valid():#не придумал как автоматическм прикрутить user к методу модели save()
                requisition = requisition_form.save()
                if  customer_initiator_form.is_valid():
                    requisition = Requisition.objects.get(id = requisition.id)
                    req_answ = RequisitionAnswer.objects.get(requisition = requisition)
                    req_answ.initiator_name = customer_initiator_form.cleaned_data['initiator_name']
                    req_answ.initiator_phone = customer_initiator_form.cleaned_data['initiator_phone']
                    req_answ.initiator_representative = customer_initiator_form.cleaned_data['initiator_representative']
                    req_answ.save()
                    return HttpResponseRedirect('/dashboard/act_list')
        except:
            HttpResponse('Что то пошло не так, проверьте не занят ли номер обращения!')



class CooperationPage(LoginRequiredMixin, View):
    model = Requisition

    def post(self, request):
        return HttpResponseRedirect('/dashboard/profile')

    def get(self, request):
        return HttpResponseRedirect('/dashboard/profile')


class Profile(LoginRequiredMixin, View):
    def get(self, request):
        performer = get_object_or_404(Performer, user=request.user)
        requisition_answer = RequisitionAnswer.objects.all().filter(performer=performer)
        return render(request, 'dashboard/profile.html', {'acts': requisition_answer,
                                                          'requisition_answer_actual':requisition_answer.filter(accepted_date=None),
                                                          'requisition_answer_accepted':requisition_answer.exclude(accepted_date=None),
                                                          'performer':performer})

class CreateAnswer(LoginRequiredMixin, View):
    def get(self, request, requisition_id):
        form = CreateAnswerForm()
        return render(request, 'dashboard/create_answer.html', {
                                                        'form':form,
                                                        'requisition_id':requisition_id
                                                        })
    def post(self, request, requisition_id):#'requisition', 'performer'
        form = CreateAnswerForm(request.POST, request.FILES)
        if form.is_valid():
            performer_document = form.cleaned_data['performer_document']
            if performer_document.size > 52428800:
                raise ValidationError('Размер файла превышает 50 мегабайт')
            else:
                answer = Answer()
                answer.performer_document = performer_document
                answer.save()
                requisition_answer = RequisitionAnswer.objects.get(requisition=requisition_id)
                requisition_answer.answer = answer
                requisition_answer.save()
                return HttpResponseRedirect('/dashboard/profile')
#доделай
