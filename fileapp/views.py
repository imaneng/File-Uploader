from django.shortcuts import get_object_or_404, redirect, render

from django.shortcuts import render
from .forms import GetFileForm
from django.http.response import JsonResponse
from .models import File
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods 

@login_required(login_url='/login/')
def entry(request):
    if request.method == 'POST':
        form = GetFileForm(request.POST, request.FILES)
        
        
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = GetFileForm()
    docs = File.objects.all()
    return render(request, 'home.html', {"form": form ,"docs": docs})


def show_user_file(request,id):
    if request.method == "GET":
        file_object = get_object_or_404(File, id=id)
        result = {
            "title": file_object.title,
            "upload_date": file_object.upload_date,
            # "uploader": file_object.uploader,
            # "duc" : file_object.duc
        }
        return JsonResponse({"status": "successful", "data": result})
    else:
        return JsonResponse({"status": "error", "msg": "faghat get mojazeh"}, status=403)





# @require_http_methods(["GET", "POST"])
# def loging(request):
#     if request.method == "GET":
#         ctx = {}
#         return render(request, "login.html", ctx)
#     else:
#         username = request.POST.get("username","" )
#         password = request.POST.get("password","" )
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             return redirect('home')
    



# def logout_view(request):
#     logout(request)
#     return redirect('home')
