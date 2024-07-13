from django.shortcuts import render, redirect
from django.views import View
from .models import Contacts, Services, Products, Reviews
# Create your views here.

class IndexView(View):
    def get(self, request):
        services = Services.objects.all()
        products = Products.objects.all()
        reviews = Reviews.objects.all()
        context = {'services': services, 'products': products, 'reviews': reviews}
        return render(request, 'index.html', context)



class ContactView(View):
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contacts.objects.create(name=name, email=email, message=message)

        return redirect('main:index')


