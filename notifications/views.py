from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Notification, Driver


# Vista para recibir notificaciones desde el ESP32
@csrf_exempt
def receive_notification(request):
    if request.method == 'POST':
        event_type = request.POST.get('event_type')
        description = request.POST.get('description', '')

        notification = Notification.objects.create(
            event_type=event_type,
            description=description
        )

        return JsonResponse({'status': 'success', 'notification_id': notification.id})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

# Vista para listar todas las notificaciones
def notifications_list(request):
    notifications = Notification.objects.all()
    return render(request, 'notifications/notifications_list.html', {'notifications': notifications})



# Vista para listar todos los conductores
def drivers_list(request):
    drivers = Driver.objects.all()
    return render(request, 'notifications/drivers_list.html', {'drivers': drivers})

def combined_view(request):
    notifications = Notification.objects.all()
    drivers = Driver.objects.all()
    return render(request, 'notifications/combined_view.html', {
        'notifications': notifications,
        'drivers': drivers  })



def home(request):
    return render(request, 'notifications/home.html')