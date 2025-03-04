from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from courses.views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDeleteAPIView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include(router.urls)),
                  path('api/lessons/', LessonListAPIView.as_view(), name='lesson-list'),
                  path('api/lessons/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
                  path('api/lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-detail'),
                  path('api/lessons/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson-update'),
                  path('api/lessons/<int:pk>/delete/', LessonDeleteAPIView.as_view(), name='lesson-delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
