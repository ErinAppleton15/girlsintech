from django.conf.urls import url
from . import views

def post_list(request):
    return render(request, 'blog/post_list.html', {})

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
