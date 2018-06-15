from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    
    context = {"users": Users.onjects.all()}
    return render(request, "users_login/index.html", context)

# Create your views here.
