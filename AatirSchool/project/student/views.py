from django.shortcuts import render
from django.utils import timezone
from .forms import *
from .models import *

def school_details(request):
    # data = school_detail.objects.filter()
    # data = school_detail.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # context = {
    #     "data": data
    # }
    return render(request, 'base.html')


