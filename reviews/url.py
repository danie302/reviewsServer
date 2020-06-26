from rest_framework import routers
from .views import CitiesView, ReviewsView

router = routers.DefaultRouter()
router.register('reviews/cities', CitiesView, 'cities')
router.register('reviews/review', ReviewsView, 'reviews')

urlpatterns = router.urls