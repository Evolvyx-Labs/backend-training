from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .services.url_shortener import  shorten_url
from .models import Urls
from django.forms.models import model_to_dict
from django.http import HttpResponse
import requests




 
def short_url(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        url = data.get('long_url')
        try:
            res = requests.head(url)
            if (res.status_code==200):
                hash = (shorten_url(url))
                if(Urls.objects.filter(short_url=hash)):
                    url_obj= Urls.objects.filter( orignal_url = url , short_url = hash ).first()
                else:
                    url_obj = Urls.objects.create( orignal_url = url , short_url = hash )
                result = model_to_dict(url_obj)
                return JsonResponse({'result': result})
            else:
                return JsonResponse({'error': 'Url does not exists'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'})
            

@csrf_exempt
def redirect_to_long_url(request,s_url):
    if request.method == 'HEAD':
        return HttpResponse(status=200)
    link = Urls.objects.filter(short_url=s_url).first()
    if(link):
        link.clicks +=1
        link.save()
    return redirect(link.orignal_url)


def list_records (request):
    records = Urls.objects.all().order_by('-created_at')
    records_dict = [model_to_dict(record) for record in records]
    return JsonResponse({'records':records_dict})