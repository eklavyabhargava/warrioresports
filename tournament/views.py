from django.shortcuts import render
from .models import Update, tdmtournament, classictournament, classic, tdm as teamdeathmatch
from .forms import tdmform, classicform
import datetime
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    updates = Update.objects.all()
    return render(request, 'index.html', {'updates': updates})

def tdm(request):
    t = tdmtournament.objects.all()
    if request.method == "POST":
        # get all submitted data
        form = tdmform(request.POST)
        # validate form
        if form.is_valid():
            player = form.save(commit=False)
            player.time = datetime.datetime.now()
            pubg_id = player.pubg_id
            duplicity = 0

            if duplicity == 0:
                player.save()
                subject = 'Thanks For Participating'
                message = f'Hi {player.name}, Thanks for participating in TDM tournament. It will be held on {t[0]}'
                email_from = settings.EMAIL_HOST_USER
                recipient = [player.email, ]
                send_mail(subject, message, email_from, recipient)

                return render(request, 'success.html', {'player': player})
    else:
        form = tdmform()
    return render(request, 'tdm.html', {'form': form, 'time': t})

def classic(request):
    t = classictournament.objects.all()
    if request.method == "POST":
        # get all submitted data
        form = classicform(request.POST)
        # validate form
        if form.is_valid():
            player = form.save(commit=False)
            player.time = datetime.datetime.now()
            player.save()
            subject = 'Thanks For Participating'
            message = f'Hi {player.name}, Thanks for participating in Classic tournament. It will be held on {t[0]}'
            email_from = settings.EMAIL_HOST_USER
            recipient = [player.email, ]
            send_mail(subject, message, email_from, recipient)

            return render(request, 'success.html', {'player': player})
    else:
        form = classicform()
    return render(request, 'classic.html', {'form': form, 'time': t})