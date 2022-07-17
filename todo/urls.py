from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('todos',views.TodoViewSet)

urlpatterns = router.urls