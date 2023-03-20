from django.urls import path

from api.views import ShortLinkApiView

app_name = 'api'

urlpatterns = [
    path('create/', ShortLinkApiView.as_view()),

]