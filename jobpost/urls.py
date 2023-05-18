"""jobpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.first),
    path('index',views.index),
    path('dash',views.dash),
    path('addreg',views.addreg),
    path('regi',views.regi),
    path('logint',views.logint,name="logint"),
    path('login',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('apply/<int:id>',views.apply,name="apply"),
  
    path('apply/jobposts',views.jobposts,name="jobposts"),

    
    path('viewpost',views.viewpost,name="viewpost"),
    
    
    path('addpost',views.addpost,name="addpost"),
    path('addjobrole',views.addjobrole,name="addjobrole"),
    path('post',views.post,name="post"),
    path('jobrole',views.jobrole,name="jobrole"),
    
    
    path('viewjobpost',views.viewjobpost,name="viewjobpost"),
    path('viewjobadmin',views.viewjobadmin,name="viewjobadmin"),
    path('viewapplications/<int:id>',views.viewapplications,name="viewapplications"),
    path('viewapplicationss/<int:id>',views.viewapplicationss,name="viewapplicationss"),
    path('deletejobpost/<int:id>',views.deletejobpost,name="deletejobpost"),
    path('download_resume/<str:resume>',views.download_resume,name="download_resume"),
    
    
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
