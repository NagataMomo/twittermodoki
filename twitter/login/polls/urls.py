from django.conf.urls import url
from . import views
from .forms import LoginForm
from django.contrib.auth.views import login, logout
# いまのバージョンでは文章ではかけないから編集した。
# login /logout を付け加えた。

# appname を付け加えること。
# main:login

app_name = 'polls'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^regist_save/$', views.regist_save, name='regist_save'),
    url(r'^add/$', views.add, name='add'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^login/$', login,{'template_name': 'polls/login.html', 'authentication_form': LoginForm},name='login'),
# 要素が四つ存在したからエラーがでたのかも。

    url(r'^logout/$',logout ,
        {'template_name': 'polls/logout.html'},
        name='logout')
        ]
