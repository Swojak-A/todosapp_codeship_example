from django.conf.urls import url, include

# from .views import index

urlpatterns = [
    # url('', index),
    url(r'^todos/', include('todos.urls', namespace='todos')),
]
