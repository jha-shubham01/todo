from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("api/todo", views.TODOViewSet, basename="todo")
urlpatterns = router.urls
