"""care URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

import portal.urls
# from portal import views
from portal import urls
urlpatterns = [
	url(r'^$', RedirectView.as_view(url=reverse_lazy('quick-select-state'))),
	url(r'^admin/', admin.site.urls),
	url(r'^login/$', views.login, {'template_name': 'registration/login.html'}, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^portal/', include(portal.urls.urlpatterns)),
	# url('policy/', include(portal.urls.urlpatterns)),

	# url(r'^policy/$',include(portal.urls.urlpatterns))
]