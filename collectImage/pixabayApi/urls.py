from django.conf.urls import url
from . import views

app_name = "pixabayApi"

urlpatterns = [
    url(r'^$', views.hello_world, name='hello_world'),
    url(r'^template/$', views.indexTemplate, name='indexTemplate'),  # 追加する
]