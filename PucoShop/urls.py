"""PucoShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from puco import views
from django.conf import settings
from django.conf.urls.static import static
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import handler404
from puco.views import mi_error_404
'''try:
    from django.conf.urls.defaults import url
except ImportError:
    from django.conf.urls import url
from .views import verificacion


urlpatterns = [
    url(r'^verificacion/$', verificacion, name='khipu_verificacion'),
]'''
handler404 = mi_error_404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('puco.urls')),
]

    

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

