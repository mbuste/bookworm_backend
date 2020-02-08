from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from books import views
from rest_framework import routers
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# router = routers.DefaultRouter()
# router.register(r'^books/$', views.BookView, 'book')


urlpatterns = [
    path('authors/', views.AuthorList.as_view()),
    path('authors/<int:pk>/', views.AuthorDetail.as_view()),
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),
    path('admin/', admin.site.urls),
    path('', include('accounts.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
