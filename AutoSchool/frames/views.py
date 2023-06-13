from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def homepage(request):
    return render(request, 'home.html')


def applications(request):
    # Активация при получении POST запроса
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        try:
            # Отправка письма
            send_mail(
                'Новая заявка',
                f'Fullname:{full_name}\nphone:{phone}\nemail:{email}',
                'omegaschool@mail.ru',
                ['omegaschool@mail.ru'],
                fail_silently=False,
            )
        except BadHeaderError:
            return HttpResponse('Некорректный заголовок письма')
        return render(request, 'apps.html')
    return render(request, 'apps.html')


def contact(request):
    return render(request, 'contacts.html')


def programs(request):
    return render(request, 'programs.html')


def org(request):
    return render(request, 'organis.html')


def shcool(request):
    return render(request, 'school.html')
