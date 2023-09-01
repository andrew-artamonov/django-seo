# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import django
from django.contrib import admin
from tests.userapp.admin import alternative_site
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^alt-admin/', alternative_site.urls),
    re_path(r'^', include('tests.userapp.urls')),
]
