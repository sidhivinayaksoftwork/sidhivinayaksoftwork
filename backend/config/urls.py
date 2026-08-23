from django.contrib import admin
from django.urls import include, path
from django.http import JsonResponse

def health(request): return JsonResponse({'status':'ok','service':'sidhivinayaksoftwork-api'})
urlpatterns = [path('admin/', admin.site.urls), path('health/', health), path('api/v1/', include('content.urls'))]

