from django.http import JsonResponse


def custom404(request, exception=None):
    return JsonResponse(data={
        "status_code":404,
        "error":"The resource was not found",
        })