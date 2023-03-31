from django.urls import path
from .import  views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
     path('register/',views.register, name='register'),
     path('translate_register/',views.customer_register.as_view(), name='translate_register'),
     path('mosque_register/',views.employee_register.as_view(), name='mosque_register'),
     path('payer_register/', views.payer_register.as_view(), name='payer_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
     path('', views.Home, name='Home'),
     path('pdf/', views.pdf, name='pdf'),
     path('panl/', views.adminpanl, name='panl'),
     path('control/', views.control, name='control'),
     path('translated/', views.transltedfile, name='translated'),
     path('uploadafter/<int:id>', views.file_after_translted, name='uploadafter'),
     path('delete_translted/<int:id>', views.delete_file_after_transleted, name='delete_translted'),
     path('delete_file/<int:id>'   ,     views.delete_file_dashboard, name='delete_file'),
     path('update/<int:id>', views.updatestates, name='update'),
     path('mousaqeF1/<int:id>', views.mousaqeF, name='mousaqeF1'),
     path('profileMo/<int:id>', views.profilemousqe, name='profileMo'),
     path('profileMo/<int:id>/?', views.profilemousqe, name='profileMo'),
     path('comment/<int:id>/', views.comment, name='comment'),
     path('comment', views.comment, name='comment'),
     path('mousaqeFiles/', views.get_mousqe_files, name='mousaqeFiles'),
     path('deletemousaqeFiles/<int:id>/', views.delete_mousaqe_files, name='deletemousaqeFiles'),

            ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)