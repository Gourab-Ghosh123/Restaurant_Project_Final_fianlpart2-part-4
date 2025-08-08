from django.shortcuts import render
from .models import Item_list, Items , Feedback , AboutUs # ✅ Import your models
from Base_app.models import BookTable


# Create your views here.


def Index(request):
    items =  Items.objects.all()
    list = Item_list.objects.all()
    review = Feedback.objects.all()
    return render(request, 'index.html',{'items': items, 'list': list , 'review' : review})

def AboutView(request):
    data = AboutUs.objects.all()
    return render(request ,'about.html' , {'data' : data})

def MenuView(request):
    list = Item_list.objects.all()
    items = Items.objects.all()
    return render(request, 'menu.html',{
        'list': list,
        'items': items
    })

def Book_TableView(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('user_email')
        total_person = request.POST.get('total_person')
        booking_date = request.POST.get('booking_date')

        if(name!= '' and phone_number != '' and email != '' and total_person != '' and booking_date != ''):
            data = BookTable(Name = name , Phone_number = len(phone_number) == 10 , Email = email , Total_person = total_person , Booking_date = booking_date)
            data.save()
    return render(request, 'book_table.html')

def FeedbackFormView(request):
    return render(request , 'feedback.html')

def CheckoutView():
    pass

def LoginView():
    pass

def LogoutView():
    pass

def GetCartItemsView():
    pass

def AddToCartView():
    pass