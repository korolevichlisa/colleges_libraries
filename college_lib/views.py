from django import http
from django.http import HttpResponse
from django.shortcuts import render
# from testdb.models import College, New, Library_funds, Room, Library_servic, Exhibition, Coworkers

# def home(request):
#     return render(request, "index.html")
    # return HttpResponse('home')


# def tfk(request):
#     news = New.objects.filter(id_college__name_college = 'Одеський технічний фаховий коледж').order_by('-published_date')[:3:-1] 
#     coworker = Coworkers.objects.filter(id_college__name_college = 'Одеський технічний фаховий коледж').values()
#     fund = Library_funds.objects.filter(id_college__name_college = 'Одеський технічний фаховий коледж').values()
#     room = Room.objects.filter(id_college__name_college = 'Одеський технічний фаховий коледж').values()
#     servivic = Library_servic.objects.filter(id_college__name_college = 'Одеський технічний фаховий коледж').values()
#     exhibition = Exhibition.objects.filter(id_college__name_college = 'Одеський технічний фаховий коледж').values()
#     return render(request, "tfk.html",{'news':news, 'coworker':coworker, 'fund':fund, 'room':room, 'servic':servivic, 'exhibition':exhibition})

# def mt(request):
#     news = New.objects.filter(id_college__name_college = 'Механіко-технологічний фаховий коледж').order_by('-published_date')[:3:-1] 
#     coworker = Coworkers.objects.filter(id_college__name_college = 'Механіко-технологічний фаховий коледж')
#     fund = Library_funds.objects.filter(id_college__name_college = 'Механіко-технологічний фаховий коледж')
#     room = Room.objects.filter(id_college__name_college = 'Механіко-технологічний фаховий коледж')
#     servivic = Library_servic.objects.filter(id_college__name_college = 'Механіко-технологічний фаховий коледж')
#     exhibition = Exhibition.objects.filter(id_college__name_college = 'Механіко-технологічний фаховий коледж')
#     return render(request, "mt.html",{'news':news, 'coworker':coworker, 'fund':fund, 'room':room, 'servic':servivic, 'exhibition':exhibition})

# def nti(request):
#     news = New.objects.filter(id_college__name_college = 'Фаховий коледж нафтогазових технологій, інженерії та інфраструктури сервісу').order_by('-published_date')[:3:-1] 
#     coworker = Coworkers.objects.filter(id_college__name_college = 'Фаховий коледж нафтогазових технологій, інженерії та інфраструктури сервісу')
#     fund = Library_funds.objects.filter(id_college__name_college = 'Фаховий коледж нафтогазових технологій, інженерії та інфраструктури сервісу')
#     room = Room.objects.filter(id_college__name_college = 'Фаховий коледж нафтогазових технологій, інженерії та інфраструктури сервісу')
#     servivic = Library_servic.objects.filter(id_college__name_college = 'Фаховий коледж нафтогазових технологій, інженерії та інфраструктури сервісу')
#     exhibition = Exhibition.objects.filter(id_college__name_college = 'Фаховий коледж нафтогазових технологій, інженерії та інфраструктури сервісу')
#     return render(request, "nti.html",{'news':news, 'coworker':coworker, 'fund':fund, 'room':room, 'servic':servivic, 'exhibition':exhibition})

# def kpa(request):
#     news = New.objects.filter(id_college__name_college = 'Коледж промислової автоматики та інформаційних технологій').order_by('-published_date')[:3:-1] 
#     coworker = Coworkers.objects.filter(id_college__name_college = 'Коледж промислової автоматики та інформаційних технологій')
#     fund = Library_funds.objects.filter(id_college__name_college = 'Коледж промислової автоматики та інформаційних технологій')
#     room = Room.objects.filter(id_college__name_college = 'Коледж промислової автоматики та інформаційних технологій')
#     servivic = Library_servic.objects.filter(id_college__name_college = 'Коледж промислової автоматики та інформаційних технологій')
#     exhibition = Exhibition.objects.filter(id_college__name_college = 'Коледж промислової автоматики та інформаційних технологій')
#     return render(request, "kpa.html",{'news':news, 'coworker':coworker, 'fund':fund, 'room':room, 'servic':servivic, 'exhibition':exhibition})