from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage, BadHeaderError, send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.utils.html import strip_tags
import logging
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)

def send_message(request):
    if request.method != 'POST':
        return redirect(request.META.get('HTTP_REFERER', '/'))

    name = strip_tags(request.POST.get('name', '')).strip() or 'İsimsiz'
    email = strip_tags(request.POST.get('email', '')).strip()
    msg = strip_tags(request.POST.get('message', '')).strip()
    source = request.POST.get('next', request.path)

    if not msg:
        messages.error(request, 'Lütfen bir mesaj yazınız.')
        return redirect(source)

    subject = 'Web Formu - Dr. Fatma Arı'
    body = f"Gönderen: {name}\nE-posta: {email or '-'}\nKaynak: {source}\n\nMesaj:\n{msg}"

    # Reply-To doğrula
    reply_to = None
    if email:
        try:
            validate_email(email)
            reply_to = [email]
        except ValidationError:
            reply_to = None

    try:
        em = EmailMessage(
            subject=subject,
            body=body,
            from_email='fatmaaribot@gmail.com',
            to=['fatmaaridr@gmail.com'],
            reply_to=reply_to,
            headers={'X-Form-Path': source},
        )
        em.send(fail_silently=False)
        messages.success(request, 'Mesajınız gönderildi. Teşekkürler.')
    except BadHeaderError:
        messages.error(request, 'Geçersiz başlık tespit edildi.')
    except Exception as e:
        logger.exception('E-posta gönderimi başarısız: %s', e)
        messages.error(request, 'Mesaj gönderilemedi. Lütfen daha sonra tekrar deneyin.')

    return redirect(source)


def hakkimda(request):
    return render(request, 'pages/hakkimda.html')