import pytest
from mixer.backend.django import mixer
from rest_framework.test import APIRequestFactory
from reviews.views import ReviewsView

@pytest.mark.django_db
class TestImages:
    def test_reviews_images_not_empty_if_city_exist(self):
        factory = APIRequestFactory()
        city = mixer.blend('reviews.City', name='djangoCity', image='testImage')
        review = mixer.blend('reviews.Review', city=city.name,  image='', id=1, review='review', traveller='python')
        request = factory.get('/reviews/review')
        view = ReviewsView.as_view({'get': 'list'})
        response = view(request)
        response.render()
        response.content.decode("utf-8")
        assert response.content.decode("utf-8") == '[{"id":1,"review":"review","city":"djangoCity","traveller":"python","image":"/media/testImage"}]'
    