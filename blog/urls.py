from django.conf.urls import url

from blog.views import SignupView

urlpatterns = [
    url(r'signup/$', SignupView.as_view(), name="signup"),
]
