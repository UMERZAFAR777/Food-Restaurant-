
from django.contrib import admin
from django.urls import path
from mysite import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('login/', views.login_view, name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_user,name='logout'),


    path('submit-table-booking/', views.submit_table_booking, name='submit_table_booking'),
    path('submit_contact_form/', views.submit_contact_form, name='submit_contact_form'),
]



if settings.DEBUG: 
    urlpatterns+=static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)




