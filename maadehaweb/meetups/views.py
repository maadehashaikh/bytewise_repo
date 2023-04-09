from django.shortcuts import render
# Create your views here.
def index(request):
    meetups=[
        { 'title': 'A first Meetup' ,
         'location':'New York',
         'slug':'a-first-meetup' },
         { 'title': 'A Second Meetup' ,
          'location':'Paris',
          'slug':'a-second-meetup'}
    ]
    return render(request,'meetups/templates/meetups/index.html',{
        'show_meetups': True,
        'meetups': meetups
    })