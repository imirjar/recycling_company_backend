from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

"""class CustomerInitiator(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=200)
    representative = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.name"""

class AnswerFile(models.Model):
    file = models.FileField(upload_to='acts/%Y/%m/%d')

class Requisition(models.Model):#Заявка от Мегафон
    number = models.CharField(max_length=50, unique=True)
    receive_date = models.DateField(blank=True, null=True)
    antennas_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    telekom_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    akb_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    iron_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    cable_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    city = models.CharField(max_length=50)
    document = models.FileField(upload_to='acts/%Y/%m/%d')

    def __str__(self):
        return self.number

    def save(self, **kwargs):
        super(Requisition, self).save(**kwargs)
        requisition_answer = RequisitionAnswer(requisition=self, answer=None,  performer=None)
        requisition_answer.save()
        return self.id

class Performer(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class Answer(models.Model):#Ответ от performer
    lom_antennas = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lom_telekom = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    akb = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    chernmet = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lom_copper = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    performer_document = models.FileField(upload_to='performer_acts/%Y/%m/%d')

    def __str__(self):
        return str(self.id)


class RequisitionAnswer(models.Model):#Модель объединяющая все в одно
    created_date = models.DateField(default = None, blank=True, null=True)
    initiator_name = models.CharField(max_length=50)
    initiator_phone = models.CharField(max_length=50)
    initiator_representative = models.CharField(max_length=50)
    requisition = models.ForeignKey(Requisition, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.SET_NULL, blank=True, null=True)
    performer = models.ForeignKey(Performer, on_delete=models.SET_NULL, blank=True, null=True)
    acceptor = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    accepted_date = models.DateField(default = None, blank=True, null=True)


    def accept(self, request):
        self.acceptor = request.user
        self.accepted_date = date.today()
        self.save()


    def decline(self, request):
        if self.acceptor: self.acceptor.delete()
        if self.accepted_date: self.accepted_date.delete()
        if self.answer: self.answer.delete()


    

#Все переименовать нормально и реализовать задумку: запрос+ответ+исполнитель с страницей для запроса и страницей для ответа по id в url
