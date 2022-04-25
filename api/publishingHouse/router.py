# # #app order
from rest_framework import routers
from api.organizations.views import OrganizationsViewSet

router = routers.DefaultRouter()

router.register('pubhouse', PublishingHouseViewSet)
router.register('textbook', TextBookViewSet)
router.register('yearpub', YearPublishingViewSet)