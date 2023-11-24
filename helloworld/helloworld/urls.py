'''
@Description: 
@Author: Panbo Hey
@Date: 2023-11-16 15:05:02
@LastEditTime: 2023-11-24 10:03:03
@LastEditors: Panbo Hey
'''

"""
URL configuration for helloworld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path



from . import views


urlpatterns = [
    
    path(r'hello', views.hello),
    path("runnoob/", views.runnoob),
    path("mytest/",views.runmuban),
    path("panbotest/",views.panbouse),
]
