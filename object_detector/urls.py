from django.urls import path

from assignment import settings
from object_detector import views
from django.conf.urls.static import static

urlpatterns = [
    path('object-detection/', views.ObjectDetector.as_view(), name='object-detection'),
    path('delete_file/<int:pk>/', views.DeleteUserFile.as_view(), name='delete_file'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)