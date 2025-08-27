from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage, BadHeaderError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.utils.html import strip_tags
import logging

logger = logging.getLogger(__name__)

def send_message(request):
    if request.method != 'POST':
        return redirect(request.META.get('HTTP_REFERER', '/'))

    # Honeypot
    if request.POST.get('website'):
        messages.info(request, 'Mesajınız alındı.')
        return redirect(request.POST.get('next', '/'))

    name = strip_tags(request.POST.get('name', '')).strip() or 'İsimsiz'
    email = strip_tags(request.POST.get('email', '')).strip()
    msg = strip_tags(request.POST.get('message', '')).strip()
    source = request.POST.get('next', request.path)

    if not msg:
        messages.error(request, 'Lütfen bir mesaj yazınız.')
        return redirect(source)

    subject = 'Web Formu - Dr. Fatma Arı'
    body = f"Gönderen: {name}\nE-posta: {email or '-'}\nKaynak: {source}\n\nMesaj:\n{msg}"

    # Reply-To için e-posta doğrula
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
            from_email=settings.DEFAULT_FROM_EMAIL,   # bot/adresiniz
            to=[settings.CONTACT_TO_EMAIL],           # hedef adres
            reply_to=reply_to,
            headers={
                'X-Form-Path': source,
            }
        )
        em.send(fail_silently=False)
        messages.success(request, 'Mesajınız gönderildi. Teşekkürler.')
    except BadHeaderError:
        messages.error(request, 'Geçersiz başlık tespit edildi.')
    except Exception as e:
        logger.exception('E-posta gönderimi başarısız: %s', e)
        messages.error(request, 'Mesaj gönderilemedi. Lütfen daha sonra tekrar deneyin.')

    return redirect(source)