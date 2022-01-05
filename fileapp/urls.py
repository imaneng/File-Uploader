



from django.urls.conf import path
from .views import entry,show_user_file

urlpatterns = [
    
    path('', entry, name= "home" ),
   
    path('show/<int:id>',show_user_file),
]
