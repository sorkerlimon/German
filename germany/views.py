from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import *
import json



def index(request):
    countries = Country.objects.all()
    locations = Location.objects.all()
    business_plans = BusinessPlan.objects.all()

    context = {
        'countries': countries,
        'locations': locations,
        'business_plans': business_plans,
    }

    return render(request, 'index.html', context)


def get_locations(request):
    country_id = request.GET.get('country_id')
    locations = Location.objects.filter(c_name=country_id)

    html = '<option value="">Select Location</option>'
    for location in locations:
        html += f'<option value="{location.id}">{location.l_name}</option>'

    return JsonResponse({'html': html})

def get_business_plans(request):
    location_id = request.GET.get('location_id')
    business_plans = BusinessPlan.objects.filter(location=location_id)

    html = '<option value="">Select Business Plan</option>'
    for business_plan in business_plans:
        html += f'<option value="{business_plan.id}">{business_plan.name}</option>'

    return JsonResponse({'html': html})




# def get_values(request):
#     business_plan_id = request.GET.get('business_plan_id')
#     business_plan = BusinessPlan.objects.get(id=business_plan_id)

#     data = {
#         'value1': business_plan.value1,
#         'value2': business_plan.value2,
#         'value3': business_plan.value3,
#     }

#     return JsonResponse(data)


def get_values(request):
    business_plan_id = request.GET.get('business_plan_id')
    business_plan = BusinessPlan.objects.get(id=business_plan_id)
    location = business_plan.location
    country = location.c_name

    data = {
        'value1': business_plan.value1,
        'value2': business_plan.value2,
        'value3': business_plan.value3,
    }

    selected_plan = SelectedPlan(
        country=country,
        location=location,
        business_plan=business_plan,
        value1=data['value1'],
        value2=data['value2'],
        value3=data['value3']
    )
    selected_plan.save()

    return JsonResponse(data)
