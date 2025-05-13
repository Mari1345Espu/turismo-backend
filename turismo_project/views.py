from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "API de Turismo en funcionamiento "})
