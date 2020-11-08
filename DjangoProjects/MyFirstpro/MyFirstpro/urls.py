
from django.contrib import admin
from django.urls import path,include


urlpatterns = [

    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('trainer/', include('trainer.urls')),
    path('mathsapp/', include('mathsapp.urls')),
    path('employee/', include('employee.urls')),
    path('students/',include('students.urls'))

]
