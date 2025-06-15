from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import SampleData

@csrf_exempt
def data_api(request):
    if request.method == 'GET':
        data = SampleData.objects.all().values('id', 'name', 'email')
        return JsonResponse(list(data), safe=False)

    elif request.method == 'POST':
        try:
            body = json.loads(request.body)
            name = body.get('name')
            email = body.get('email') #indhu.com
            if not name or not email:
                return JsonResponse({'error': 'Name and Email are required'}, status=400)
            
            emailValidation = SampleData.objects.filter(email=email)
            nameValidation =SampleData.objects.filter(name=name)
            if nameValidation.exists():
                return JsonResponse({'error': 'Name is already exsist'}, status=400)
            if emailValidation.exists():
                return JsonResponse({'error': 'email is already exsist'}, status=400)

            obj = SampleData.objects.create(name=name, email=email)
            return JsonResponse({'message': 'Data created', 'id': obj.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    elif request.method == 'PUT':
        try:
            body = json.loads(request.body)
            id=body.get('id')
            name = body.get('name')
            email = body.get('email')
            if not name or not email or not id:
                return JsonResponse({'error': 'Name , Email and ID are required'}, status=400)
            
            datas = SampleData.objects.all().values('id', 'name', 'email')
            
            obj = SampleData.objects.get(id=id)
            obj.name=name 
            obj.email=email
            obj.save()
            return JsonResponse({'message': f'{id} updated sucessfully'}, status=201)
        except Exception as e:  
            print(e)
            return JsonResponse({'error': str(e)}, status=500)
