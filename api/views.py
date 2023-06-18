from collections import Counter
from ipaddress import summarize_address_range
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from api.models import Data
from api.serializers import DataSerializer
from django.views.decorators.http import require_GET

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    
    

def total_items_sold(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    department = request.GET.get('department', 'Marketing')
    
    sales = Data.objects.filter(department=department, date__range=[start_date, end_date])
    
    total_items = sales.count()
    return JsonResponse({'total_items': total_items}) 


def nth_most_total_item_view(request):
    item_by = request.GET.get('item_by' , None)
    start_date = request.GET.get('start_date' , None)
    end_date = request.GET.get('end_date' , None)
    n = request.GET.get('n', None)
    
    item_name = "Item XYZ"
    
    return JsonResponse({'item_name' : item_name})



@require_GET
def percentage_of_department_wise_sold_items(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

  
    department_sold_items = Data.objects.annotate(total_sold_items=Counter('items__sales')).values('dept_name', 'total_sold_items')


    total_sold_items = Data.objects.aggregate(total_sold_items=summarize_address_range('items__sales'))['total_sold_items']


    department_percentages = {}
    for department in department_sold_items:
        department_name = department['dept_name']
        sold_items = department['total_sold_items']
        percentage = (sold_items / total_sold_items) * 100
        department_percentages[department_name] = round(percentage, 2)

    return JsonResponse(department_percentages)





def monthly_sales(request):
    if request.method == 'GET':
        product = request.GET.get('product')
        year = request.GET.get('year')
               
        monthly_sales_data = Data.objects.filter(product=product, year=year).values_list('amount', flat=True)
        
        monthly_sales_list = list(monthly_sales_data)
        
        return JsonResponse(monthly_sales_list, safe=False)

