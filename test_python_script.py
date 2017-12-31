"""
from django.http import HttpResponse

def trial(request):
    python_data = request.POST.get('dd')
    return HttpResponse(python_data)
"""
open("empty_file.txt", 'w')
