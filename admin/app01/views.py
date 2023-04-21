from django.shortcuts import render
from app01.models import Thumbnail


def home(request):
    """
    Tiltle page
    :param request:
    :return:
    """
    return render(request, 'home.html')


def welcome(request):
    """
    Page with selection between browsing popular selections and choosing base
    :param request:
    :return:
    """
    return render(request, 'welcome.html')


def popular(request):
    """
    Display what's in the database.
    Popu;ar selections.
    :param request:
    :return:
    """
    data_list = Thumbnail.objects.all()
    return render(request, 'popular.html', {"data_list": data_list})


def base(request):
    """
    Display choices of base alcohols.
    :param request:
    :return:
    """
    return render(request, 'base.html')


def vodka(request):
    """
    Detailed page of Vodka.
    :param request:
    :return:
    """
    full_list = Thumbnail.objects.all()
    data_list = []
    for i in full_list:
        if i.base_id == 1:
            data_list.append(i)
    return render(request, "vodka.html", {"data_list": data_list})


def whiskey(request):
    """
    Detailed page of Whiskey.
    :param request:
    :return:
    """
    full_list = Thumbnail.objects.all()
    data_list = []
    for i in full_list:
        if i.base_id == 2:
            data_list.append(i)
    return render(request, "vodka.html", {"data_list": data_list})


def rum(request):
    """
    Detailed page of Rum.
    :param request:
    :return:
    """
    full_list = Thumbnail.objects.all()
    data_list = []
    for i in full_list:
        if i.base_id == 3:
            data_list.append(i)
    return render(request, "vodka.html", {"data_list": data_list})


def tequila(request):
    """
    Detailed page of Tequila.
    :param request:
    :return:
    """
    full_list = Thumbnail.objects.all()
    data_list = []
    for i in full_list:
        if i.base_id == 4:
            data_list.append(i)
    return render(request, "vodka.html", {"data_list": data_list})


def gin(request):
    """
    Detailed page of Gin.
    :param request:
    :return:
    """
    full_list = Thumbnail.objects.all()
    data_list = []
    for i in full_list:
        if i.base_id == 5:
            data_list.append(i)
    return render(request, "vodka.html", {"data_list": data_list})


def mixed(request):
    """
    Detailed page of Mixed base.
    :param request:
    :return:
    """
    full_list = Thumbnail.objects.all()
    data_list = []
    for i in full_list:
        if i.base_id == 6:
            data_list.append(i)
    return render(request, "vodka.html", {"data_list": data_list})


def brandly(request):
    """
    Detailed page of Brandy. 
    :param request:
    :return:
    """
    full_list = Thumbnail.objects.all()
    data_list = []
    for i in full_list:
        if i.base_id == 7:
            data_list.append(i)
    return render(request, "vodka.html", {"data_list": data_list})
