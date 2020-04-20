from datetime import datetime

from django.conf import settings
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect

from web.models import Publication


def index(request):
    return render(request, 'index.html')

def contacts(request):
    return render(request, 'contacts.html')

# publications_data = [
# {
#     'id': 0,
#     'name': 'Publication One',
#     'date': datetime.now(),
#     'text':'''Sed non enim molestie, rutrum erat sit amet, viverra augue. Duis ipsum felis, ultricies ut erat fringilla, posuere viverra nibh. Suspendisse sit amet nunc quam. Pellentesque efficitur ligula dolor, non convallis mauris interdum quis. Suspendisse fringilla tortor ac iaculis pharetra. Vestibulum iaculis erat felis, porttitor vehicula justo placerat a. Nulla eu dignissim ligula, sed gravida elit. Pellentesque aliquet, augue quis tempor mattis, lacus dolor maximus erat, vitae condimentum nisi libero sed erat. Nunc at tortor pharetra, congue diam sit amet, ultricies lectus. Aenean quis maximus
#     .<br><br>Praesent leo justo, sollicitudin a maximus et, gravida dapibus lorem. Vestibulum ut nisi efficitur, consectetur tortor in, rhoncus metus. Ut magna erat, efficitur eget arcu et, fermentum vulputate augue. Integer nibh erat, tincidunt sit amet purus eu, dictum aliquet lectus. Fusce viverra, ex id iaculis vulputate, ipsum sem commodo urna, et interdum metus ante ac velit.<br><br>
#     Suspendisse mattis libero feugiat blandit accumsan. Duis feugiat dolor eu venenatis varius. Donec auctor est ac ligula dictum bibendum. Integer turpis velit, tincidunt id mattis a, suscipit quis urna. Etiam sit amet eros ut metus placerat luctus non at enim. In tincidunt et est efficitur bibendum. Aliquam erat volutpat. Phasellus ut leo sed nisl ultricies lacinia. Aliquam finibus rhoncus urna, vel elementum magna. Quisque pretium velit eget elit tincidunt, eu molestie massa interdum.'''
# },
# {
#     'id': 1,
#     'name': 'Publication Two',
#     'date': datetime.now(),
#     'text':'''Suspendisse efficitur non orci at blandit. Proin aliquam dolor nec risus viverra, ac aliquet eros molestie. Nam quis arcu vel magna commodo commodo. Vestibulum blandit justo in blandit blandit. Fusce rhoncus dui mauris.
#     <br><br>Etiam scelerisque risus eget ex suscipit aliquam. In volutpat vehicula est, vel finibus metus tristique in. Vivamus blandit posuere arcu, nec pellentesque neque mollis sit amet. Fusce varius nunc in finibus egestas. Quisque dapibus, diam eget sodales molestie, sapien risus scelerisque ante, sit amet pellentesque odio lorem et ipsum. Morbi elementum sodales tincidunt. Nunc vel sagittis mauris. Morbi sit amet porttitor turpis, in suscipit ex. Donec facilisis arcu in ante interdum, eu convallis ante pellentesque.'''
# },
# {
#     'id': 2,
#     'name': 'Publication Three',
#     'date': datetime.now(),
#     'text':'''Pellentesque efficitur ligula dolor, non convallis mauris interdum quis. Suspendisse fringilla tortor ac iaculis pharetra. Vestibulum iaculis erat felis, porttitor vehicula justo placerat a. Nulla eu dignissim ligula, sed gravida elit. Pellentesque aliquet, augue quis tempor mattis, lacus dolor maximus erat, vitae condimentum nisi libero sed erat. Nunc at tortor pharetra, congue diam sit amet, ultricies lectus. Aenean quis maximus
#     .<br><br>Praesent leo justo, sollicitudin a maximus et, gravida dapibus lorem. Vestibulum ut nisi efficitur, consectetur tortor in, rhoncus metus. Ut magna erat, efficitur eget arcu et, fermentum vulputate augue. Integer nibh erat, tincidunt sit amet purus eu, dictum aliquet lectus. Fusce viverra, ex id iaculis vulputate, ipsum sem commodo urna, et interdum metus ante ac velit.<br><br>
#     Suspendisse mattis libero feugiat blandit accumsan. <br><br>
#     Etiam sit amet eros ut metus placerat luctus non at enim. In tincidunt et est efficitur bibendum. Aliquam erat volutpat. Phasellus ut leo sed nisl ultricies lacinia. Aliquam finibus rhoncus urna, vel elementum magna. Quisque pretium velit eget elit tincidunt, eu molestie massa interdum.'''
# },
# ]

def publish(request):
    if request.method == 'GET':
        return render(request, 'publish.html')
    else:
        secret = request.POST['secret']
        name = request.POST['name']
        text = request.POST['text']

        if secret != settings.SECRET_KEY:
            return render(request, 'publish.html', {
                'error': 'wrong Secret Key'
            })
        if len(name) == 0:
            return render(request, 'publish.html', {
                'error': 'Empty name'
            })
        if len(text) == 0:
            return render(request, 'publish.html', {
                'error': 'Empty text'
            })

        # publications_data.append({
        #     'id': len(publications_data),
        #     'name': name,
        #     'date': datetime.now(),
        #     'text': text.replace('\n', '<br />')
        # })

        Publication(
            name=name,
            date=datetime.now(),
            text=text.replace('\n', '<br />')).save()

        return redirect('/publications')

def publications(request):
    return render(request, 'publications.html', {
        'publications':Publication.objects.all()
    })

def publication(request, number):
    pubs = Publication.objects.filter(id=number)


    if len(pubs) == 1:
        pub = model_to_dict(pubs[0])
        return render(request, 'publication.html', pub)
    else:
        return redirect('/')

def ststus(request):
    return HttpResponse('<h3>OK</h3>')