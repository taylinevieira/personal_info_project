from django.http import JsonResponse
from datetime import datetime

def welcome (request):
    return JsonResponse ({"message":"Welcome to the Personal info API!"})

def goodbye (request):
    return JsonResponse ({"message":"Goodbye, see you next time!"})

def current_time (request):
    now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    return JsonResponse({"current_time": now})

def greet (request):
    name = request.GET.get ("name", "Stranger")
    return JsonResponse ({"message": f"Hello, {name}!"})

def age_category(request):
    age = request.GET.get("age")
    if not age:
        return JsonResponse({"error": "Missing 'age' parameter."}, status=400)
    try:
        age = int(age)
        if age <= 12:
            category = "Child"
        elif age <= 17:
            category = "Teenager"
        elif age <= 59:
            category = "Adult"
        else:
            category = "Senior"
        return JsonResponse({"category": category})
    except ValueError:
        return JsonResponse({"error": "Invalid age input."}, status=400)

def sum_view(request, num1, num2):
    try:
        total = int(num1) + int(num2)
        return JsonResponse({"sum": total})
    except ValueError:
        return JsonResponse({"error": "Invalid input, please provide two integers."})