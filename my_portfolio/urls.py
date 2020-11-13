
from django.contrib import admin
from django.urls import path
import my_portfolio.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_portfolio.views.homepage, name="homepage"),
]
