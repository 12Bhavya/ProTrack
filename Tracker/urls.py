from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'), #Login screen
    url(r'^authentication/$', views.login_next, name='login_next'), #Login screen Validation
    url(r'^signup/$',views.signup,name='signup'),
    
    url(r'^homepage/$', views.homepage, name='homepage'),
    url(r'^add_group/$',views.add_group, name='add_group'), 
    url(r'^add_project/$',views.add_project, name='add_project'),
    url(r'^add_task/$',views.add_task, name='add_task'),
    url(r'^add_sprint/$',views.add_sprint, name='add_sprint'),
	url(r'^add_comment/$',views.add_comment, name='add_comment'),
	url(r'^task_comment/(?P<task_id>[0-9]+)/$',views.task_comment, name='task_comment'),
    url(r'^add_tag/$',views.add_tag, name='add_tag'),
    url(r'^search_tag/$',views.search_tag, name='search_tag'),
	url(r'^task_tag/(?P<task_id>[0-9]+)/$',views.task_tag, name='task_tag'),
    url(r'^edit_group/(?P<group_id>[0-9]+)/$',views.edit_group, name='edit_group'),
    url(r'^edit_project/(?P<project_id>[0-9]+)/$',views.edit_project, name='edit_project'),
    url(r'^edit_task/(?P<task_id>[0-9]+)/$',views.edit_task, name='edit_task'),
    url(r'^chart/(?P<project_id>[0-9]+)/$',views.pieview, name='chart'),
    url(r'^edit_sprint/(?P<sprint_id>[0-9]+)/$',views.edit_sprint, name='edit_sprint'),
    ]

