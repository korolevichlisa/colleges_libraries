from django import http
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from testdb.models import College, New, Library_funds, Library_room, Library_servic, Exhibition, Coworkers, Photos


def home(request):
    return render(request, "index.html")

def tfk(request):
    news = New.objects.filter(id_college__name_college = 'Одеський технічний фаховий коледж').order_by('-published_date')[:3:-1] 
    coworker = Coworkers.objects.filter(id_college__name_college = 'Одеський технічний фаховий коледж').order_by('-published_date')[::-1]
    fund = Library_funds.objects.filter(id_college__name_college = 'Одеський технічний фаховий коледж')
    room = Library_room.objects.filter(id_college__name_college = 'Одеський технічний фаховий коледж')
    print(room)
    post = get_object_or_404(room)
    photos = Photos.objects.filter(post = post)
    servivic = Library_servic.objects.filter(id_college__name_college = 'Одеський технічний фаховий коледж')
    exhibition = Exhibition.objects.filter(id_college__name_college = 'Одеський технічний фаховий коледж')
    return render(request, "tfk.html",{'news':news, 'coworker':coworker, 'fund':fund, 'room':room, 'photos':photos, 'servic':servivic, 'exhibition':exhibition})

def mt(request):
    news = New.objects.filter(id_college__name_college = 'Механіко-технологічний фаховий коледж').order_by('-published_date')[:3:-1] 
    coworker = Coworkers.objects.filter(id_college__name_college = 'Механіко-технологічний фаховий коледж')
    fund = Library_funds.objects.filter(id_college__name_college = 'Механіко-технологічний фаховий коледж')
    room = Library_room.objects.filter(id_college__name_college = 'Механіко-технологічний фаховий коледж')
    post = get_object_or_404(room)
    photos = Photos.objects.filter(post = post)
    servivic = Library_servic.objects.filter(id_college__name_college = 'Механіко-технологічний фаховий коледж')
    exhibition = Exhibition.objects.filter(id_college__name_college = 'Механіко-технологічний фаховий коледж')
    return render(request, "mt.html",{'news':news, 'coworker':coworker, 'fund':fund, 'room':room,'photos':photos, 'servic':servivic, 'exhibition':exhibition})

def nti(request):
    news = New.objects.filter(id_college__name_college = 'Фаховий коледж нафтогазових технологій, інженерії та інфраструктури сервісу').order_by('-published_date')[:3:-1] 
    coworker = Coworkers.objects.filter(id_college__name_college = 'Фаховий коледж нафтогазових технологій, інженерії та інфраструктури сервісу')
    fund = Library_funds.objects.filter(id_college__name_college = 'Фаховий коледж нафтогазових технологій, інженерії та інфраструктури сервісу')
    room = Library_room.objects.filter(id_college__name_college = 'Фаховий коледж нафтогазових технологій, інженерії та інфраструктури сервісу')
    post = get_object_or_404(room)
    photos = Photos.objects.filter(post = post)
    servivic = Library_servic.objects.filter(id_college__name_college = 'Фаховий коледж нафтогазових технологій, інженерії та інфраструктури сервісу')
    exhibition = Exhibition.objects.filter(id_college__name_college = 'Фаховий коледж нафтогазових технологій, інженерії та інфраструктури сервісу')
    return render(request, "nti.html",{'news':news, 'coworker':coworker, 'fund':fund, 'room':room, 'photos':photos, 'servic':servivic, 'exhibition':exhibition})

def kpa(request):
    news = New.objects.filter(id_college__name_college = 'Коледж промислової автоматики та інформаційних технологій').order_by('-published_date')[:3:-1] 
    coworker = Coworkers.objects.filter(id_college__name_college = 'Коледж промислової автоматики та інформаційних технологій')
    fund = Library_funds.objects.filter(id_college__name_college = 'Коледж промислової автоматики та інформаційних технологій')
    room = Library_room.objects.filter(id_college__name_college = 'Коледж промислової автоматики та інформаційних технологій')
    post = get_object_or_404(room)
    photos = Photos.objects.filter(post = post)
    servivic = Library_servic.objects.filter(id_college__name_college = 'Коледж промислової автоматики та інформаційних технологій')
    exhibition = Exhibition.objects.filter(id_college__name_college = 'Коледж промислової автоматики та інформаційних технологій')
    return render(request, "kpa.html",{'news':news, 'coworker':coworker, 'fund':fund, 'room':room, 'photos':photos, 'servic':servivic, 'exhibition':exhibition})