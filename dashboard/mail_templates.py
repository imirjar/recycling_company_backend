from django.core.mail import send_mail
from django.conf import settings

def send_apointment_mail(req_answ):
    title = 'Акт приема-передачи'
    body = 'Вы выбраны в качестве исполнителя по акту приема-передачи № %s. \n Перейдите по ссылке www.vtormet-resurs.ru и зайдите в личный кабинет в правом верхнем углу экрана'%req_answ.requisition.number
    send_mail(title, body, settings.EMAIL_HOST_USER, [req_answ.performer.user.email])

def send_decline_mail(req_answ):
    title = 'Успешное завершение'
    body = 'Акт № %s отклонен!\n Просьба уточнить у менеджера причину.'%req_answ.requisition.number
    send_mail(title, body, settings.EMAIL_HOST_USER, [req_answ.performer.user.email])

def send_acception_mail(req_answ):
    title = 'Успешное завершение'
    body = 'Акт № %s успешно завершен!\n Благодарим вас за сотрудничество!'%req_answ.requisition.number
    send_mail(title, body, settings.EMAIL_HOST_USER, [req_answ.performer.user.email])
