from django.urls import path
from .views import hello

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', hello),
]