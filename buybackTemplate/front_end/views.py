from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {"title":"Hello World!"}
    return render(request, "index.html", context)