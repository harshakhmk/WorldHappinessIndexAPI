from django.http import HttpResponse, JsonResponse

def error404(request, exception):
    
    return JsonResponse({
        'status_code': 404,
        'error': 'The resource was not found on this url'
    },safe=False,status=404)

def error500(request):
    return JsonResponse({
        'status_code': 500,
        'error': 'Internal Server Error'
    },safe=False)

def error400(request, exception):
    return JsonResponse({
        'status_code': 400,
        'error': 'Bad Request'
    },status=status.HTTP_400_BAD_REQUEST)
def error403(request, exception):
    return JsonResponse({
        'status_code': 403,
        'error': 'Request Forbidden'
    },status=status.HTTP_403_FORBIDDEN)
