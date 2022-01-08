from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse


def otp_email(username,cost,paymethod, reciver):
    subject = 'Request Approval'
    message = 'Hello '+username + \
        ' We have approved your requesr on repaire.It will cost you '+cost + ' and our payment method is '+paymethod+' please do the necessary in accordance to to your method of pay'
    from_email = 'info@goldlinebreeze.com'
    try:
        send_mail(subject, message, from_email, [reciver])
        print('sent')
    except BadHeaderError:
        return HttpResponse('Invalid header found.')