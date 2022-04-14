from rest_framework.routers import DefaultRouter

from book.views import (
    AuthorViewSet,
    PublisherViewSet,
    BookViewSet,
    SalesViewSet
)

router = DefaultRouter()

router.register(r'authors', AuthorViewSet, basename='authors')
router.register(r'publishers', PublisherViewSet, basename='publishers')
router.register(r'books', BookViewSet, basename='books')
router.register(r'sales', SalesViewSet, basename='sales')
urlpatterns = router.urls
