from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from books import views
from rest_framework import routers
from django.urls import path,include

# router = routers.DefaultRouter()
# router.register(r'^books/$', views.BookView, 'book')


urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),
    path('admin/', admin.site.urls),
    path('', include('accounts.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
