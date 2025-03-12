from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from courses.views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDeleteAPIView
from users.views import UserViewSet, UserRegisterAPIView, UserDetailAPIView, PaymentViewSet, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'users', UserViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include(router.urls)),
                  path('api/register/', UserRegisterAPIView.as_view(), name='register'),
                  path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('api/users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
                  path('api/lessons/', LessonListAPIView.as_view(), name='lesson-list'),
                  path('api/lessons/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
                  path('api/lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-detail'),
                  path('api/lessons/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson-update'),
                  path('api/lessons/<int:pk>/delete/', LessonDeleteAPIView.as_view(), name='lesson-delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
