# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.urls import re_path

from .views import page_detail, product_detail, tag_detail, my_view, my_other_view


urlpatterns = [
    re_path(r'^pages/([\w\d-]+)/', page_detail, name="userapp_page_detail"),
    re_path(r'^products/(\d+)/', product_detail, name="userapp_product_detail"),
    re_path(r'^tags/(.+)/', tag_detail, name="userapp_tag"),
    re_path(r'^my/view/(.+)/', my_view, name="userapp_my_view"),
    re_path(r'^my/other/view/(.+)/', my_other_view, name="userapp_my_other_view"),
]
