from django.urls import path
from .views import home,about,BlogView,contact,faq,project_details,project,review,service_details,service,single_blog,health,sport,product
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',home,name='home'),
    path('about',about,name='about'),
    path('blog',BlogView,name='blog'),
    path('contact',contact,name='contact'),
    path('faq',faq,name='faq'),
    path('project_details/<int:id>',project_details,name='project_details'),
    path('project',project,name='project'),
    path('review',review,name='review'),
    path('service_details/<int:id>',service_details,name='service_details'),
    path('service',service,name='service'),
    path('single_blog/<int:id>',single_blog,name='single_blog'),
    path('health',health,name='health'),
    path('soprt',sport,name='sport'),
    path('product',product,name='product'),



    
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
